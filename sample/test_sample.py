import unittest
import os

# patchtestdata is the module that contains PatchTestInput class, used as
# a namespace to store patchtest command line arguments like the repo directory
# or the series/revision being tested
from patchtestdata import PatchTestInput as pti

class TestSample(unittest.TestCase):

    def pretest_sample(self):
        """ Sample test: test that runs before patching"""
        self.assertTrue(True)

    def test_sample(self):
        """ Sample test: test that runs after patching """
        self.assertTrue(True)

