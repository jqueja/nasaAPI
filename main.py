from requests import get
from pprint import PrettyPrinter
printer = PrettyPrinter()


# https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY
def main():
    data = get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY').json()
    printer.pprint(data)




main()
