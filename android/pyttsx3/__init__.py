import os
import sh
from pythonforandroid.logger import shprint, info
from pythonforandroid.util import current_directory
from os.path import join

from pythonforandroid.recipe import PythonRecipe

class Pyttsx3Recipe(PythonRecipe):
	version = '2.92'
	url = 'http://kimird.com/pymodules/pyttsx3-2.92.tar.gz'
	depends = ['python3']
	site_packages_name = 'pyttsx3'
	call_hostpython_via_targetpython = False

recipe = Pyttsx3Recipe()
