import os
from os.path import join

from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class UJsonRecipe(CompiledComponentsPythonRecipe):
	version = '1.35'
	url = 'https://pypi.python.org/packages/source/u/ujson/ujson-{version}.tar.gz'
	depends = ['hostpython3']
	call_hostpython_via_targetpython = False

	def get_recipe_env(self, arch):
		env = super().get_recipe_env(arch)
		curdir = os.path.abspath(os.path.dirname(__file__))
		py_include = join(self.ctx.get_python_install_dir(arch.arch), 'include')
		sqlit_include = self.get_recipe('sqlite3', self.ctx).get_build_dir(arch.arch) 
		env['CFLAGS'] += f' -I{curdir} -I{py_include} -I{sqlit_include} '
		return env


recipe = UJsonRecipe()
