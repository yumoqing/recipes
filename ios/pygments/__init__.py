
from kivy_ios.toolchain import PythonRecipe
class pygmentsRecipe(PythonRecipe):
   version = "2.12.0"
   url = "https://files.pythonhosted.org/packages/59/0f/eb10576eb73b5857bc22610cdfc59e424ced4004fe7132c8f2af2cc168d3/Pygments-2.12.0.tar.gz"
   depends = ["python"]

recipe = pygmentsRecipe()
