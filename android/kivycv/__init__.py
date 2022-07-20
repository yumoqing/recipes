import os
import sh
from pythonforandroid.logger import shprint, info
from pythonforandroid.util import current_directory
from os.path import join

from pythonforandroid.recipe import PythonRecipe

class KivycvRecipe(PythonRecipe):
	version = '0.1.0'
	url = 'http://kimird.com/pymodules/kivycv-0.1.0.tar.gz'
	depends = ['python3', 'kivyblocks', 'opencv']
	site_packages_name = 'kivycv'
	call_hostpython_via_targetpython = False

recipe = KivycvRecipe()
