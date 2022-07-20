from kivy_ios.recipes.pypi_info import get_version_url
from kivy_ios.toolchain import PythonRecipe
class apppublicRecipe(PythonRecipe):
   # version, url = get_version_url('apppublic')
   version = "5.1.16"
   url = 'http://kimird.com/pymodules/appPublic-5.1.16.tar.gz'
   depends = ["python"]

recipe = apppublicRecipe()
