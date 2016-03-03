import unittest
import os

# patchtestdata is the module that contains PatchTestInput class, used as
# a namespace to store patchtest command line arguments like the repo directory
# or the series/revision being tested
from patchtestdata import PatchTestInput as pti

class TestSample(unittest.TestCase):

    def test_repodir_existance(self):
        """ Sample test: checks that the repository exists """
        self.assertTrue(os.path.exists(pti.repodir))

    @unittest.skipUnless(pti.repo.items, "There are no items to test")
    def test_items_non_empty(self):
        """ Sample test: check items have content """
        # An Repo's item is an abstraction of either a series or mbox.
        for item in pti.repo.items:
            self.assertFalse(item.is_empty, "Item should not be empty")

