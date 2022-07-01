from os.path import join, dirname, abspath
import sh
from pythonforandroid.recipe import NDKRecipe
from pythonforandroid.util import current_directory
from pythonforandroid.logger import shprint
from multiprocessing import cpu_count


class PARecipe(NDKRecipe):
	'''
    test recipe
	'''
	version = '1.48.04'
	url = 'http://sourceforge.net/projects/espeak/files/espeak/espeak-1.48/espeak-1.48.04-source.zip'
	depends = ['portaudio']
	patches = []
	generated_libraries = [
		'libespek.so'
		'libespek.a'
	]


	def get_recipe_env(self, arch):
		env = super().get_recipe_env(arch)
		par = self.get_recipe('portaudio', self.ctx)
		pa = par.get_build_dir(arch.arch)
		portaudio_include = join(pa, 'include')
		portaudio_lib = pa
		env['ANDROID_NDK'] = self.ctx.ndk_dir
		env['ANDROID_SDK'] = self.ctx.sdk_dir
		env['CXXFLAGS'] += f' -I{portaudio_include}'
		env['LDFLAGS'] += f' -L{portaudio_lib}'
		return env

	def build_arch(self, arch):
		build_dir = join(self.get_build_dir(arch.arch), 'src')
		with current_directory(build_dir):
			env = self.get_recipe_env(arch)
			python_major = self.ctx.python_recipe.version[0]
			python_include_root = self.ctx.python_recipe.include_root(arch.arch)
			python_site_packages = self.ctx.get_site_packages_dir(arch)
			python_link_root = self.ctx.python_recipe.link_root(arch.arch)
			python_link_version = self.ctx.python_recipe.major_minor_version_string
			if 'python3' in self.ctx.python_recipe.name:
				python_link_version += 'm'
			python_library = join(python_link_root,
								  'libpython{}.so'.format(python_link_version))

			shprint(sh.make, env=env)
			# Install python bindings (cv2.so)
			sh.cp(sh.glob('./lib*.so'),
				  self.ctx.get_libs_dir(arch.arch))
			sh.cp(sh.glob('../espeak-data/*'),
					self.ctx.get_libs_dir(arch.arch))


recipe = PARecipe()

