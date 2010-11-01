import subprocess
import sys
import unittest
from os.path import dirname
from ..utils import compile_thrift
from mudserve.serialize import Serializer

class TestSerializer(unittest.TestCase):
	def setUp(self):
		compile_thrift("serialize.thrift")
		from serialize.ttypes import TestObj
		self.cls = TestObj
		self.serializer = Serializer(TestObj)
	
	def testSerialize(self):
		inst = self.cls(name="test", id=5)
		str = self.serializer.to_string(inst)
		obj = self.serializer.from_string(str)
		assert obj.name == "test"
		assert obj.id == 5

if __name__ == "__main__":
	unittest.main()
