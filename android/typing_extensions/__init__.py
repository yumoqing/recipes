import os
import sh
from pythonforandroid.logger import shprint, info
from pythonforandroid.util import current_directory
from os.path import join

from pythonforandroid.recipe import PythonRecipe

class ARecipe(PythonRecipe):
	version = '4.3.0'
	url = 'http://kimird.com/pymodules/typing_extensions-4.3.0.tar.gz'
	depends = ['python3']
	site_packages_name = 'typing_extensions'
	call_hostpython_via_targetpython = False

recipe = ARecipe()
