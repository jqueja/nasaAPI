from requests import get
from pprint import PrettyPrint
printer = PrettyPrinter()


def formulateDate(year, month, day):
    date = year + '-' + month + '-' + day
    
    return date
