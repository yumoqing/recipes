
from kivy_ios.toolchain import PythonRecipe
class xlrdRecipe(PythonRecipe):
   version = "2.0.1"
   url = "https://files.pythonhosted.org/packages/a6/b3/19a2540d21dea5f908304375bd43f5ed7a4c28a370dc9122c565423e6b44/xlrd-2.0.1.tar.gz"
   depends = ["python"]

recipe = xlrdRecipe()
