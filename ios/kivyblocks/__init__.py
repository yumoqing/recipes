
from kivy_ios.toolchain import PythonRecipe
class kivyblocksRecipe(PythonRecipe):
   version = "0.2.6"
   url = "https://files.pythonhosted.org/packages/89/d7/939caad1a1e5568dab0283cdaadbfa747bfae811ea0cd46744a5590c31fc/kivyblocks-0.2.6.tar.gz"
   depends = ["python", "kivy"]

recipe = kivyblocksRecipe()
