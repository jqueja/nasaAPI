import unittest
from funcs import *

class TestFuncs(unittest.TestCase):

    def test(self):
        msg = "testing date formulation"

        year = '2016'
        month = '06'
        day = '05'

        self.assertEqual(formulateDate(year, month, day), '2016-06-05', msg)
