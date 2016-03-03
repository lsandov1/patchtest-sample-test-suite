import unittest

# patchtestdata is the module that contains PatchTestInput class, used as
# a namespace to store patchtest command line arguments like the repo directory
# or the series/revision being tested
from patchtestdata import PatchTestInput as pti

class TestSample(unittest.TestCase):

    def test_repodir_existance(self):
        self.assertTrue(os.path.exists(pti.repodir))

    def test_items_non_empty(self):
        # An Repo's item is an abstraction of either a series or mbox.
        for item in pti.repo.items:
            self.assertFalse(item.is_empty, "Item should not be empty")

