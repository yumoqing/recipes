import os
import os
import sh
from kivy_ios.toolchain import PythonRecipe, shprint


class UJsonRecipe(PythonRecipe):
	version = "5.3.0"
	url = 'https://files.pythonhosted.org/packages/92/38/a8c8d8cdacd586e0e66673ca60daf295a79cd5b4fae72a25f1bfa482554d/ujson-5.3.0.tar.gz'
	depends = ["python", "setuptools" ]

	def install(self):
		arch = list(self.filtered_archs)[0]
		build_dir = self.get_build_dir(arch.arch)
		os.chdir(build_dir)
		hostpython = sh.Command(self.ctx.hostpython)
		build_env = arch.get_env()
		dest_dir = os.path.join(self.ctx.dist_dir, "root", "python")
		build_env['PYTHONPATH'] = os.path.join(dest_dir, 'lib', 'python3.7', 'site-packages')
		shprint(hostpython, "setup.py", "build_ext", "--prefix", dest_dir, _env=build_env)
		shprint(hostpython, "setup.py", "install", "--prefix", dest_dir, _env=build_env)


recipe = UJsonRecipe()
