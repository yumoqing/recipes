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
	version = '2.0'
	url = 'https://github.com/yumoqing/portaudio/archive/master.zip'
	depends = []
	patches = []
	generated_libraries = [
		'libportaudio.so'
		'libportaudio.a'
	]


	def get_recipe_env(self, arch):
		env = super().get_recipe_env(arch)
		env['ANDROID_NDK'] = self.ctx.ndk_dir
		env['ANDROID_SDK'] = self.ctx.sdk_dir
		return env

	def build_arch(self, arch):
		build_dir = join(self.get_build_dir(arch.arch), 'build')
		shprint(sh.mkdir, '-p', build_dir)

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

			shprint(sh.cmake,
					'-DP4A=ON',
					'-DANDROID_ABI={}'.format(arch.arch),
					'-DANDROID_STANDALONE_TOOLCHAIN={}'.format(self.ctx.ndk_dir),
					'-DANDROID_NATIVE_API_LEVEL={}'.format(self.ctx.ndk_api),
					'-DANDROID_EXECUTABLE={}/tools/android'.format(env['ANDROID_SDK']),

					'-DCMAKE_TOOLCHAIN_FILE={}'.format(
						join(self.ctx.ndk_dir, 'build', 'cmake',
							 'android.toolchain.cmake')),
					# Force to build as shared libraries the cv2's dependant
					# libs or we will not be able to link with our python
					'-DBUILD_SHARED_LIBS=ON',
					'-DCMAKE_SHARED_LINKER_FLAGS=-L%s' % abspath(dirname(__file__)) ,
					'-DBUILD_STATIC_LIBS=OFF',
					self.get_build_dir(arch.arch),
					_env=env)
			shprint(sh.make)
			# Install python bindings (cv2.so)
			sh.cp(sh.glob('./lib*.so'),
				  self.ctx.get_libs_dir(arch.arch))


recipe = PARecipe()
