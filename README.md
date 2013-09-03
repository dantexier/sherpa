Sherpa/Romeo
============

Get the list journals Sherpa/Romeo


Sherpa/Romeo has an  list of journals alphabetically ordered, and for each letter there are approximately 2000 journals in groups of 50 to 50. 
The goal is to get title, ISSN, ESSN, and Romeo Color

The list is at: http://www.sherpa.ac.uk/romeo/journalbrowse.php?la=en&fIDnum=&mode=simple

The base code is of @pudo, and, is at: https://github.com/pudo/hhba-scraping

# Problems

When I do several connections, appears a problem "max retries exceeded", so, 
the scraping I have to do it for parts.

The error is:
requests.exceptions.ConnectionError: HTTPConnectionPool(host='www.sherpa.ac.uk', port=80): 
Max retries exceeded with url: /romeo/journalbrowse.php?la=en&fIDnum=%7C&mode=simple 
(Caused by <class 'socket.gaierror'>: [Errno -2] Name or service not known)
