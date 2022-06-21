
from kivy_ios.toolchain import PythonRecipe
class nanoidRecipe(PythonRecipe):
   version = "2.0.0"
   url = "https://files.pythonhosted.org/packages/b7/9d/0250bf5935d88e214df469d35eccc0f6ff7e9db046fc8a9aeb4b2a192775/nanoid-2.0.0.tar.gz"
   depends = ["python"]

recipe = nanoidRecipe()
