import os
import sh
from pythonforandroid.logger import shprint, info
from pythonforandroid.util import current_directory
from os.path import join

from pythonforandroid.recipe import PythonRecipe

class KivychartsRecipe(PythonRecipe):
	version = '0.0.9'
	url = 'http://kimird.com/pymodules/kivycharts-0.0.9.tar.gz'
	depends = ['python3', 'kivyblocks']
	site_packages_name = 'kivycharts'
	call_hostpython_via_targetpython = False

recipe = KivychartsRecipe()
