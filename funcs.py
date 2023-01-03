from requests import get
from pprint import PrettyPrinter
printer = PrettyPrinter()


def formulateDate(year, month, day):
    date = year + '-' + month + '-' + day

    return date
