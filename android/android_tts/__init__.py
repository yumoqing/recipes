import os
import sh
from pythonforandroid.logger import shprint, info
from pythonforandroid.util import current_directory
from os.path import join

from pythonforandroid.recipe import PythonRecipe

class ARecipe(PythonRecipe):
	version = '5.1.16'
	url = 'http://kimird.com/pymodules/android_tts-0.0.1.tar.gz'
	depends = ['python3', 'pyttsx3']
	site_packages_name = 'android_tts'
	call_hostpython_via_targetpython = False

recipe = ARecipe()
