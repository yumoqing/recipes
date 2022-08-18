import os
import sh
from pythonforandroid.logger import shprint, info
from pythonforandroid.util import current_directory
from pythonforandroid.recipes.pypi_info import get_version_url
from os.path import join

from pythonforandroid.recipe import PythonRecipe

class ApppublicRecipe(PythonRecipe):
	# version = '5.1.16'
	# url = 'http://kimird.com/pymodules/appPublic-5.1.16.tar.gz'
	version, url = get_version_url('apppublic')
	depends = ['python3']
	call_hostpython_via_targetpython = False

recipe = ApppublicRecipe()
