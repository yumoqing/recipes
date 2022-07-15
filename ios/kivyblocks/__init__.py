from kivy_ios.recipes.pypi_info import get_version_url
from kivy_ios.toolchain import PythonRecipe
class kivyblocksRecipe(PythonRecipe):
   version = "0.2.16"
   url = "http://kimird.com/pymodules/kivyblocks-0.2.16.tar.gz"
   # version, url = get_version_url('kivyblocks')
   depends = ["python", "kivy"]

recipe = kivyblocksRecipe()
