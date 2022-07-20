
from kivy_ios.toolchain import PythonRecipe
from kivy_ios.recipes.pypi_info import get_version_url
class TmpRecipe(PythonRecipe):
   version, url = get_version_url('pyobjc', version='')
   depends = ["python"]

recipe = TmpRecipe()
