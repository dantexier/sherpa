import requests
from lxml import html
from pprint import pprint
from urlparse import urljoin

# A list of all journals in Sherpa/Romeo
BASE_URL = 'http://www.sherpa.ac.uk/romeo/journalbrowse.php?la=en&fIDnum=|&mode=simple'

def prueba():

    # Download the list.
    response = requests.get(BASE_URL)

    # Parse HTML
    document = html.fromstring(response.content)

    # Get all the page first (there are 50 journals of 2328) by letter A:
    for link in document.cssselect('table.journaltable a'):
        print (link.get('href'))
        # But, I want to get title, ISSN, ESSN, and, Romeo Colour for each journal

if __name__ == '__main__':
    prueba()
