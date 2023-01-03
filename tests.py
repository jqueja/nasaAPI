import unittest
from funcs import *
from pprint import PrettyPrinter
printer = PrettyPrinter()

class TestFuncs(unittest.TestCase):

    def testFormulateDate(self):
        msg = "testing date formulation"

        year = '2016'
        month = '06'
        day = '05'

        self.assertEqual(formulateDate(year, month, day), '2016-06-05', msg)

    def testCheckURL1(self):
        msg = "testing bad format"

        startDate = '2016-06-07'
        endDate = '2016-06-15'

        BASE_URL = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + startDate + '&end_date=' + endDate + '&api_key=DEMO_KEY'
        data = get(BASE_URL).json()

        self.assertEqual(checkURL(data), False, msg)

    def testCheckURL2(self):
        msg = "testing no data"

        startDate = '1800-06-07'
        endDate = '1800-06-14'

        BASE_URL = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + startDate + '&end_date=' + endDate + '&api_key=DEMO_KEY'
        data = get(BASE_URL).json()

        self.assertEqual(checkURL(data), False, msg)

    def testCheckURL3(self):
        msg = "testing correct format"

        startDate = '2016-06-07'
        endDate = '2016-06-14'

        BASE_URL = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + startDate + '&end_date=' + endDate + '&api_key=DEMO_KEY'
        data = get(BASE_URL).json()

        self.assertEqual(checkURL(data), True, msg)
