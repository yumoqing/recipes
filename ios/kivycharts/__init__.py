
from kivy_ios.toolchain import PythonRecipe
class kivychartsRecipe(PythonRecipe):
   version = "0.0.9"
   url = "https://files.pythonhosted.org/packages/94/4d/b0ec2cc64a43d2706a0ccab973118aa1b5d5b171d6a212e75ac2fa6f50c5/kivycharts-0.0.9.tar.gz"
   depends = ["python"]

recipe = kivychartsRecipe()
