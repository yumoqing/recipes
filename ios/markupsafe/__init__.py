
from kivy_ios.toolchain import PythonRecipe
from kivy_ios.recipes.pypi_info import get_version_url
class markupsafeRecipe(PythonRecipe):
   version, url = get_version_url('markupsafe')
   depends = ["python"]

recipe = markupsafeRecipe()
