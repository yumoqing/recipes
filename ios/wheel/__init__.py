
from os.path import join
from kivy_ios.toolchain import HostRecipe, shprint, cache_execution
from kivy_ios.recipes.pypi_info import get_version_url
from kivy_ios.context_managers import cd, python_path
import sh

class TempRecipe(HostRecipe):
	depends = ["openssl", "hostpython3", "python3", "host_setuptools3"]
	version, url = get_version_url('wheel')

	@cache_execution
	def install(self):
		arch = self.filtered_archs[0]
		build_dir = self.get_build_dir(arch.arch)
		hostpython = sh.Command(self.ctx.hostpython)

		with python_path(self.ctx.site_packages_dir):
			with cd(build_dir):
				python_prefix = join(self.ctx.dist_dir, 'hostpython3')
				shprint(hostpython, "setup.py", "install",
						f"--prefix={python_prefix}")

recipe = TempRecipe()
