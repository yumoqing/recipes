
from kivy_ios.toolchain import PythonRecipe
class kivychartsRecipe(PythonRecipe):
   version = "0.0.9"
   url = "http://kimird.com/pymodules/kivycharts-0.0.9.tar.gz"
   depends = ["python"]

recipe = kivychartsRecipe()
