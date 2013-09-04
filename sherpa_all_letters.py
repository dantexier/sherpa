import requests
from lxml import html
from lxml import etree
from pprint import pprint
from urlparse import urljoin

# A list of all journals in Sherpa/Romeo
BASE_URL = 'http://www.sherpa.ac.uk/romeo/journalbrowse.php?la=en&fIDnum=|&mode=simple'
CAD_01 = 'http://www.sherpa.ac.uk/romeo/journalbrowse.php?pageno='
CAD_02 = 'la=en&fIDnum=|&mode=simple&letter='
Letter = [['B',21],['C',38],['D',9],['E',25],['F',10],['G',10],['H',10],['I',54],['J',74],['K',3],['L',8],['M',19],['N',$

def prueba():
    #25 without Z
    count_letter = 24
    j = 0
    while j < count_letter:
        j = j + 1
        maximo = Letter [j][1]
        i = 0
        while i < maximo:
            i = i + 1
            CADENA = CAD_01 + str(i) + '&' + CAD_02 + Letter[j][0]
            response = requests.get(CADENA)
            document = html.fromstring(response.content)
            for link in document.cssselect('table.journaltable tr'):
                print(etree.tostring(link))

if __name__ == '__main__':
    prueba()
