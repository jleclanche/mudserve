import unittest
import sys
from os.path import join
from subprocess import call
from . import serializer

TESTS_PATH = "./tests/"
GEN_PATH = "gen-py/"

# Make sure the generated thrift files are on the python path
sys.path.insert(0, join(TESTS_PATH, GEN_PATH))

# Create our suite
suite = unittest.TestSuite((serializer.suite,))

# Run it with the standard runner
runner = unittest.TextTestRunner()
runner.run(suite)

# Don't edit this without knowing what you're doing
call(["rm", "-rf", join(TESTS_PATH, GEN_PATH)])
