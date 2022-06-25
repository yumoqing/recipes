from kivy_ios.recipes.pypi_info import get_version_url
from kivy_ios.toolchain import PythonRecipe
class kivyblocksRecipe(PythonRecipe):
   # version = "0.2.8"
   # url = "https://files.pythonhosted.org/packages/29/0c/0a47536a0692df84663ea1f659f5106df12f1041bbff163cec7aeae41809/kivyblocks-0.2.8.tar.gz"
   version, url = get_version_url('kivyblocks')
   depends = ["python", "kivy"]

recipe = kivyblocksRecipe()
