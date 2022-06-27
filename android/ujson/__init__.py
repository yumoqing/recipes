import os
from os.path import join
from pythonforandroid.logger import info, debug, shprint, warning
from pythonforandroid.recipe import PythonRecipe


class UJsonRecipe(PythonRecipe):
	version = '1.35'
	url = 'https://pypi.python.org/packages/source/u/ujson/ujson-{version}.tar.gz'
	depends = ['hostpython3']
	call_hostpython_via_targetpython = False
	info('=============START ujson================================')

	def get_recipe_env(self, arch):
		env = super().get_recipe_env(arch)
		recipe_dir = os.path.dirname(__file__)
		env['CFLAGS'] += ' -I{recipe_dir}'
		info('=============================================')
		info('env add CFLAGS={}'.format(env['CFLAGS']))
		info('=============================================')
		return env

recipe = UJsonRecipe()
