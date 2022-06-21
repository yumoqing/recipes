
from kivy_ios.toolchain import PythonRecipe
class apppublicRecipe(PythonRecipe):
   version = "5.1.10"
   url = "https://files.pythonhosted.org/packages/d3/b2/74168e50ec657b0051d21794a4264c388e046adfd74e3c3cb8c50758a2a4/appPublic-5.1.10.tar.gz"
   depends = ["python"]

recipe = apppublicRecipe()
