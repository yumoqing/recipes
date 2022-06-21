import os
import os
import sh
from kivy_ios.toolchain import PythonRecipe, shprint


class BrotliRecipe(PythonRecipe):
	version = "1.0.9"
	url = 'https://files.pythonhosted.org/packages/2a/18/70c32fe9357f3eea18598b23aa9ed29b1711c3001835f7cf99a9818985d0/Brotli-1.0.9.zip'
	depends = []

	def install(self):
		arch = list(self.filtered_archs)[0]
		build_dir = self.get_build_dir(arch.arch)
		os.chdir(build_dir)
		hostpython = sh.Command(self.ctx.hostpython)
		build_env = arch.get_env()
		dest_dir = os.path.join(self.ctx.dist_dir, "root", "python")
		build_env['PYTHONPATH'] = os.path.join(dest_dir, 'lib', 'python3.7', 'site-packages')
		shprint(hostpython, "setup.py", "build_ext", _env=build_env)
		shprint(hostpython, "setup.py", "install", _env=build_env)


recipe = BrotliRecipe()
