import unittest

# patchtestdata is the module that contains the patchtest command line arguments
# and  input data (either series or local mboxes)
import patchtestdata

pti = patchtestdata.PatchTestInput.pti

class SignedOff(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # An item is an abstraction of either a series or mbox.
        # patchtest can test more than one item at a time, so items variable
        # is a list
        cls.items = pti.repo.items

    def test_presence(self):
        self.assertTrue(True)
