import unittest
from OSDetector import detect_os

class TestOSDetector(unittest.TestCase):
def test_detect_os(self):
os_name = detect_os()
self.assertIn(os_name, ["Windows", "Linux", "MacOS"])

if __name__ == '__main__':
unittest.main()
