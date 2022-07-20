import os
import sh
from pythonforandroid.logger import shprint, info
from pythonforandroid.util import current_directory
from os.path import join

from pythonforandroid.recipe import PythonRecipe

class KivyblocksRecipe(PythonRecipe):
	version = '0.2.16'
	url = 'http://kimird.com/pymodules/kivyblocks-0.2.16.tar.gz'
	depends = ['python3', 'kivy']
	site_packages_name = 'kivyblocks'
	call_hostpython_via_targetpython = False

recipe = KivyblocksRecipe()
