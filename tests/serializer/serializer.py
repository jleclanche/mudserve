import subprocess
import sys
import unittest
from os.path import dirname
from ..utils import compile_thrift, get_tempfile
from mudserve.serialize import Serializer

class TestSerializer(unittest.TestCase):
	def setUp(self):
		compile_thrift("serialize.thrift")
		from serialize.ttypes import TestObj
		self.cls = TestObj
		self.serializer = Serializer(TestObj)
	
	def test_str(self):
		inst = self.cls(name="test", id=5)
		str = self.serializer.to_string(inst)
		obj = self.serializer.from_string(str)
		assert obj == inst
		
	def test_file(self):
		f = get_tempfile()
		inst = self.cls(name="test", id=6)
		str = self.serializer.to_file(inst, f.name)
		obj = self.serializer.from_file(f.name)
		assert obj == inst

if __name__ == "__main__":
	unittest.main()
