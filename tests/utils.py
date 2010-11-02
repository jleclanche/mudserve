from os.path import dirname, abspath
from subprocess import call
from sys import _getframe
from tempfile import NamedTemporaryFile
from . import constants

def compile_thrift(file, up=1):
	"""
	Utility method to compile a thrift file existing in a subdirectory while
	placing the output in tests/gen-py.
	"""
	
	args = ["thrift", "--gen", "py:new_style", "-o",
			dirname(abspath(__file__)), file]
	cwd = abspath(_getframe(1).f_code.co_filename)
	call(args, cwd=dirname(cwd))

def get_tempfile(mode="rw+b"):
	return NamedTemporaryFile(mode=mode, dir=constants.TMP_PATH, delete=False)
