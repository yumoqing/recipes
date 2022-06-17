import os
from os.path import join

from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class UJsonRecipe(CompiledComponentsPythonRecipe):
	version = '1.35'
	url = 'https://pypi.python.org/packages/source/u/ujson/ujson-{version}.tar.gz'
	depends = ['hostpython3']
	call_hostpython_via_targetpython = False

recipe = UJsonRecipe()
