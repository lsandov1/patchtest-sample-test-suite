import unittest

# patchtestdata is the module that contains the patchtest command line arguments
# and  input data (either series or local mboxes)
import patchtestdata

patchtestinput = patchtestdata.PatchtestInput.pti

class SignedOff(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # An item is an abstraction of either a series or mbox.
        # patchtest can test more than one item at a time, so items variable
        # is a list
        cls.items = patchtestinput.repo.items

    def test_presence(self):
        self.assertTrue(True)
