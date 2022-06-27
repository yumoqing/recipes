
from kivy_ios.toolchain import PythonRecipe
from kivy_ios.recipes.pypi_info import get_version_url
class jinja2Recipe(PythonRecipe):
   version, url = get_version_url('jinja2')
   depends = ["python"]

recipe = jinja2Recipe()
