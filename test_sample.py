import unittest
import os
import logging

# PatchTestInput contains patchtest input data
from patchtestdata import PatchTestInput as pti

# PatchTestDataStore is used to share data between unit tests
from patchtestdata import PatchTestDataStore as ptds

# patchtest logger
logger = logging.getLogger('patchtest')

class TestSample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info('Test Sample Suite')

    def pretest_sample(self):
        """ Sample test: test that runs before patching"""
        ptds['sample'] = True
        self.assertTrue(True)

    def test_sample(self):
        """ Sample test: test that runs after patching """
        self.assertTrue(ptds['sample'])

