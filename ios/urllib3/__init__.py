
from kivy_ios.toolchain import PythonRecipe
class urllib3Recipe(PythonRecipe):
   version = "1.26.9"
   url = "https://files.pythonhosted.org/packages/1b/a5/4eab74853625505725cefdf168f48661b2cd04e7843ab836f3f63abf81da/urllib3-1.26.9.tar.gz"
   depends = ["python"]

recipe = urllib3Recipe()
