import os
import sh
from pythonforandroid.logger import shprint, info
from pythonforandroid.util import current_directory
from os.path import join

from pythonforandroid.recipe import PythonRecipe

class PyaudioRecipe(PythonRecipe):
	version = '0.2.11'
	url = 'https://files.pythonhosted.org/packages/ab/42/b4f04721c5c5bfc196ce156b3c768998ef8c0ae3654ed29ea5020c749a6b/PyAudio-0.2.11.tar.gz'
	depends = ['python3', 'portaudio']
	site_packages_name = 'pyaudio'
	call_hostpython_via_targetpython = False

	def get_recipe_env(self, arch):
		env = super().get_recipe_env(arch)
		curdir = os.path.abspath(os.path.dirname(__file__))
		portaudio_build = self.get_recipe('portaudio', self.ctx).get_build_dir(arch.arch)
		portaudio_include = join(portaudio_build, 'include')
		py_include = join(self.ctx.get_python_install_dir(arch.arch), 'include')
		sqlit_include = self.get_recipe('sqlite3', self.ctx).get_build_dir(arch.arch) 
		env['CFLAGS'] += f' -I{curdir} -I{py_include} -I{sqlit_include} -I{portaudio_include} '
		env['LDFLAGS'] += f' -L{portaudio_build}'
		info('=====================info pyaudio======================')
		shprint(sh.echo, "pyaudio ====CFLAGS=", env['CFLAGS'], arch.arch)
		shprint(sh.echo, "pyaudio ====LDFLAGS", env['LDFLAGS'], arch.arch)
		info('===========================================')
		return env

recipe = PyaudioRecipe()
