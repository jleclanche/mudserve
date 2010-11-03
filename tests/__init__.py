import sys
from os import mkdir
from shutil import rmtree
from subprocess import call
from unittest import TestSuite, TextTestRunner
from . import constants

# Test suites
from . import serializer

# Make sure the generated thrift files are on the python path
sys.path.insert(0, constants.GEN_PATH)

# Create our suite
suite = TestSuite((serializer.suite,))

# Run it with the standard runner
runner = TextTestRunner()
runner.run(suite)

# Delete the created folders
rmtree(constants.GEN_PATH)
rmtree(constants.TMP_PATH)
