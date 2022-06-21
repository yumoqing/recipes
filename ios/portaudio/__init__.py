from kivy_ios.toolchain import Recipe, shprint
from kivy_ios.context_managers import cd
from os.path import join, dirname, abspath
import sh
import os
import fnmatch

class PortaudioRecipe(Recipe):
	'''
	test recipe
	'''
	version = '19.7.0'
	url = 'http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz'
	patches = []
	library = "libportaudio.a"
	# include_per_arch = True


	def build_arch(self, arch):
		build_env = arch.get_env()
		configure = sh.Command(join(self.build_dir, "configure"))
		shprint(configure,
				"CC={}".format(build_env["CC"]),
				"LD={}".format(build_env["LD"]),
				"CFLAGS={}".format(build_env["CFLAGS"]),
				"LDFLAGS={}".format(build_env["LDFLAGS"]),
				"--prefix=/",
				"--host={}".format(arch.triple),
				"--disable-shared")
		shprint(sh.make, 'clean')
		shprint(sh.make, self.ctx.concurrent_make)

recipe = PortaudioRecipe()
