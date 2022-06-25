from kivy_ios.recipes.pypi_info import get_version_url
from kivy_ios.toolchain import PythonRecipe
class apppublicRecipe(PythonRecipe):
   version, url = get_version_url('apppublic')
   # version = "5.1.11"
   # url = "https://files.pythonhosted.org/packages/5b/72/ce266e01e92b989172b7fc2fc9633c316af2e8c36876a50bf5a6d04b1c05/appPublic-5.1.11.tar.gz"
   depends = ["python"]

recipe = apppublicRecipe()
