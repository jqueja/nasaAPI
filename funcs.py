from requests import get
from pprint import PrettyPrinter
printer = PrettyPrinter()


def formulateDate(year, month, day):
    date = year + '-' + month + '-' + day

    return date

def checkURL(dct):
    try:
        if dct['code'] == 400:
            return False
    except KeyError:
        if dct['element_count'] == 0:
            print('There is no data')
            return False
        else:
            return True

def getData(startDate, endDate):
    BASE_URL = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=' + startDate + '&end_date=' + endDate + '&api_key=DEMO_KEY'
    data = get(BASE_URL).json()
    return data

def printTable():
    pass
