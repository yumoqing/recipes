
from kivy_ios.toolchain import PythonRecipe
from kivy_ios.recipes.pypi_info import get_version_url
class qrcodeRecipe(PythonRecipe):
   version, url = get_version_url('qrcode')
   depends = ["python"]

recipe = qrcodeRecipe()
