import os
import sh
from pythonforandroid.logger import shprint, info
from pythonforandroid.util import current_directory
from os.path import join

from pythonforandroid.recipe import CompiledComponentsPythonRecipe
# from pythonforandroid.recipe import PythonRecipe

class PyaudioRecipe(CompiledComponentsPythonRecipe):
	version = '0.2.11'
	url = 'https://files.pythonhosted.org/packages/ab/42/b4f04721c5c5bfc196ce156b3c768998ef8c0ae3654ed29ea5020c749a6b/PyAudio-0.2.11.tar.gz'
	depends = ['portaudio']
	site_packages_name = 'pyaudio'
	call_hostpython_via_targetpython = False

	def get_recipe_env(self, arch):
		env = super().get_recipe_env(arch)
		curdir = os.path.abspath(os.path.dirname(__file__))
		portaudio_include = join(self.get_recipe('portaudio', self.ctx).get_build_dir(arch.arch), 'include')
		py_include = join(self.ctx.get_python_install_dir(arch.arch), 'include')
		sqlit_include = self.get_recipe('sqlite3', self.ctx).get_build_dir(arch.arch) 
		env['CFLAGS'] += f' -I{curdir} -I{py_include} -I{sqlit_include} -I{portaudio_include} '
		shprint(sh.echo, env['CFLAGS'])
		return env

	def install_python_package(self, arch):
		'''Automate the installation of a Python package (or a cython
		package where the cython components are pre-built).'''
		env = self.get_recipe_env(arch)

		info('Installing {} into site-packages, env={}'.format(self.name, env))

		with current_directory(self.get_build_dir(arch.arch)):
			hostpython = sh.Command(self.ctx.hostpython)
			info('hostpython={}'.format(hostpython))
			shprint(hostpython, 'setup.py', 'install', '-O2', _env=env)

	def build_arch(self, arch):
		super().build_arch(arch)
		self.install_python_package(arch)

recipe = PyaudioRecipe()
