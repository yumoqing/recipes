# import sys
# sys.path.append('..')
# from portaudio import recipe as pa_recipe
from os.path import join
from pythonforandroid.toolchain import shprint
import sh
from pythonforandroid.recipe import Recipe, CompiledComponentsPythonRecipe


class PyAudioRecipe(CompiledComponentsPythonRecipe):
	url = 'https://github.com/yumoqing/pyaudio/archive/master.zip'
	depends = ['portaudio']

	def get_recipe_env(self, arch):
		env = super().get_recipe_env(arch)
		pa_recipe = Recipe.get_recipe('portaudio', self.ctx)
		portaudio_include = join(pa_recipe.get_build_dir(arch.arch), 'include')

		crypt_h_path = join(self.ctx.bootstrap.build_dir,
				'jni',
				'SDL2_image', 
				'external',
				'zlib-1.2.11',
				'contrib',
				'minizip')
		env['CRYPE_H_PATH'] = crypt_h_path
		env['CFLAGS'] += f' -I{crypt_h_path} -I{portaudio_include} '
		shprint(sh.echo, crypt_h_path)
		return env


recipe = PyAudioRecipe()
