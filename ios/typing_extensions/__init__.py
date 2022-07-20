
from kivy_ios.toolchain import PythonRecipe
from kivy_ios.recipes.pypi_info import get_version_url
class TmpRecipe(PythonRecipe):
   # version, url = get_version_url('typing_extensions', version='')
   version = '4.3.0'
   url = 'http://kimird.com/pymodules/typing_extensions-4.3.0.tar.gz'
   depends = ["python"]

recipe = TmpRecipe()
