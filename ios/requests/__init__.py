
from kivy_ios.toolchain import PythonRecipe
class requestsRecipe(PythonRecipe):
   version = "2.28.0"
   url = "https://files.pythonhosted.org/packages/e9/23/384d9953bb968731212dc37af87cb75a885dc48e0615bd6a303577c4dc4b/requests-2.28.0.tar.gz"
   depends = ["python", "urllib3", "charset_normalizer", "idna"]

recipe = requestsRecipe()
