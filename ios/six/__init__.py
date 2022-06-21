
from kivy_ios.toolchain import PythonRecipe
class sixRecipe(PythonRecipe):
   version = "1.15.0"
   url = "https://pypi.python.org/packages/source/s/six/six-{version}.tar.gz"
   depends = ["python"]

recipe = sixRecipe()
