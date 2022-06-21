
from kivy_ios.toolchain import PythonRecipe
class idnaRecipe(PythonRecipe):
   version = "3.3"
   url = "https://files.pythonhosted.org/packages/62/08/e3fc7c8161090f742f504f40b1bccbfc544d4a4e09eb774bf40aafce5436/idna-3.3.tar.gz"
   depends = ["python"]

recipe = idnaRecipe()
