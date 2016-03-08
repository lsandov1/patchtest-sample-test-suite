import unittest
import os

# PatchTestInput contains patchtest input data
from patchtestdata import PatchTestInput as pti

# PatchTestDataStore is used to share data between unit tests
from patchtestdata import PatchTestDataStore as ptds

class TestSample(unittest.TestCase):

    def pretest_sample(self):
        """ Sample test: test that runs before patching"""
        ptds['sample'] = True
        self.assertTrue(True)

    def test_sample(self):
        """ Sample test: test that runs after patching """
        self.assertTrue(ptds['sample'])

