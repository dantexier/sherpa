import requests
from lxml import html
from lxml import etree
from pprint import pprint
from urlparse import urljoin

# A list of all journals in Sherpa/Romeo
BASE_URL = 'http://www.sherpa.ac.uk/romeo/journalbrowse.php?la=en&fIDnum=|&mode=simple'
CAD_01 = 'http://www.sherpa.ac.uk/romeo/journalbrowse.php?pageno='
CAD_02 = 'la=en&fIDnum=|&mode=simple&letter='


def prueba():

    # Download the list.
    response = requests.get(BASE_URL)

    # Parse HTML
    document = html.fromstring(response.content)

    # Get all the page first (there are 50 journals of 2328) by letter A:
    for link in document.cssselect('table.journaltable tr'):
        #print (link)
        print(etree.tostring(link))

    maximo = 47
    i = 1
    while i < maximo:
        i = i + 1
        CADENA = CAD_01 + str(i) + '&' + CAD_02 + 'C'
        response = requests.get(CADENA)
        document = html.fromstring(response.content)
        for link in document.cssselect('table.journaltable tr'):
            print(etree.tostring(link))

if __name__ == '__main__':
    prueba()
