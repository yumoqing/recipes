
from kivy_ios.toolchain import PythonRecipe
from kivy_ios.recipes.pypi_info import get_version_url
class TmpRecipe(PythonRecipe):
   #version, url = get_version_url('pyttsx3', version='')
   version = '2.92'
   url = 'http://kimird.com/pymodules/pyttsx3-2.92.tar.gz'
   depends = ["python"]

recipe = TmpRecipe()
