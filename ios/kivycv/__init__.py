
from kivy_ios.toolchain import PythonRecipe
from kivy_ios.recipes.pypi_info import get_version_url
class TmpRecipe(PythonRecipe):
   #version, url = get_version_url('kivycv', version='')
   version = '0.1.0'
   url = 'http://kimird.com/pymodules/kivycv-0.1.0.tar.gz'
   depends = ["python"]

recipe = TmpRecipe()
