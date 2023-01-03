from requests import get
from pprint import PrettyPrinter
from funcs import *
printer = PrettyPrinter()


# https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY
def main():
    print('Date Format Exception - Expected format (yyyy-mm-dd) - The Feed date limit is only 7 Days')

    startYear = input('Enter a start year: ')
    startMonth = input('Enter a start month: ')
    startDay = input('Enter a start day: ')
    print()

    endYear = input('Enter an end year: ')
    endMonth = input('Enter an end month: ')
    endDay = input('Enter an end day: ')
    print()

    startDate = formulateDate(startYear, startMonth, startDay)
    endDate = formulateDate(endYear, endMonth, endDay)

    data = getData(startDate, endDate)

    if checkURL(data) == False:
        print('Please try again')
        main()
    else:
        printer.pprint(data['near_earth_objects'])



main()
