from os.path import dirname, realpath
from kivy_ios.toolchain import PythonRecipe
from kivy_ios.recipes.pypi_info import get_version_url
class TmpRecipe(PythonRecipe):
	version, url = get_version_url('cryptography', version='3.3.2')
	depends = ["python"]

	def get_recipe_env(self, arch):
		env = super().get_recipe_env()
		recipe_dir = realpath(dirname(__file__))
		env['CFLAGS'] += f' -I{recipe_dir}'
		return env

recipe = TmpRecipe()
