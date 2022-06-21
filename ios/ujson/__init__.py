import os
import sh
from os.path import join
import fnmatch
from kivy_ios.toolchain import PythonRecipe, shprint
import logging
logger = logging.getLogger(__name__)

class UJsonRecipe(PythonRecipe):
	version = "4.0.0"
	url = 'https://files.pythonhosted.org/packages/93/f1/b57ed26d5a971a41e18def43cecdfc36440e5aea13b379556f233b4757ac/ujson-4.0.0.tar.gz'
	depends = ["python", "setuptools" ]

	def env_min(self, env, arch):
		if arch.arch == 'x86_64':
			env['CFLAGS'] = ''.join(env['CFLAGS'].split('-miphoneos-version-min=8.0'))
			env['LDFLAGS'] = ''.join(env['LDFLAGS'].split('-miphoneos-version-min=8.0'))
		else:
			env['CFLAGS'] = ''.join(env['CFLAGS'].split('-mmacosx-version-min=10.12'))
			env['LDFLAGS'] = ''.join(env['LDFLAGS'].split('-mmacosx-version-min=10.12'))
		return env
		
	def get_ujson_env(self, arch):
		build_env = arch.get_env()
		build_env["IOSROOT"] = self.ctx.root_dir
		build_env["IOSSDKROOT"] = arch.sysroot
		# build_env["LDSHARED"] = join(self.ctx.root_dir, "tools", "liblink")
		build_env["ARM_LD"] = build_env["LD"]
		build_env["ARCH"] = arch.arch
		build_env["C_INCLUDE_PATH"] = join(arch.sysroot, "usr", "include")
		build_env["LIBRARY_PATH"] = join(arch.sysroot, "usr", "lib")
		build_env['PATH'] = os.environ['PATH']
		env = self.env_min(build_env, arch)
		return env

	def build_arch(self, arch):
		build_env = self.get_ujson_env(arch)
		hostpython3 = sh.Command(self.ctx.hostpython)
		dest_dir = os.path.join(self.ctx.dist_dir, "root", "python3")
		logger.info('+++++++++++++++++BUILD_ARCH+++++++++++++++++++++')
		logger.info('arch={},build_env={}'.format(arch.arch, build_env))
		logger.info('dest_dir={}'.format(dest_dir))
		logger.info('======================================')
		shprint(hostpython3, "setup.py", "build_ext", _env=build_env)
		self.biglink()

	def install(self):
		arch = list(self.filtered_archs)[0]
		build_dir = self.get_build_dir(arch.arch)
		os.chdir(build_dir)
		hostpython3 = sh.Command(self.ctx.hostpython)
		build_env = self.get_ujson_env(arch)
		dest_dir = join(self.ctx.dist_dir, "root", "python3")
		build_env['PYTHONPATH'] = join(dest_dir, 'lib', 'python3.9', 'site-packages')
		dest_dir = os.path.join(self.ctx.dist_dir, "root", "python3")
		logger.info('+++++++++++++++++INSTALL+++++++++++++++++++++')
		logger.info('arch={},build_env={}'.format(arch.arch, build_env))
		logger.info('dest_dir={}'.format(dest_dir))
		logger.info('======================================')
		shprint(hostpython3, "setup.py", "install", "--prefix", dest_dir,
				_env=build_env)

	def biglink(self):
		dirs = []
		for root, dirnames, filenames in os.walk(self.build_dir):
			if fnmatch.filter(filenames, "*.so.libs"):
				dirs.append(root)
		cmd = sh.Command(join(self.ctx.root_dir, "tools", "biglink"))
		shprint(cmd, join(self.build_dir, "libiujson.a"), *dirs)


recipe = UJsonRecipe()
