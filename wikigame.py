import sys
import urllib2,cookielib
import mechanize
import re
from bs4 import BeautifulSoup

def get_html(url):
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    request = urllib2.Request(url, headers=header)

    try:
        br = mechanize.Browser()
        response = br.open(request)
        return response.get_data()
    
    except urllib2.HTTPError, e:
        print e.fp.read()

class wikiPage:
    def __init__(self, state, parent):
        # Use page link as state.
        self.state = state
        self.parent = parent

    def get_children(self):
        resultHTML = get_html(self.state)
        bodySoup = BeautifulSoup(resultHTML)
        body = bodySoup.find('div', { 'class' : 'mw-content-ltr', 'id' : 'mw-content-text' })

        content = BeautifulSoup(str(body))
        allLinks = content.find_all('a')
        children = []
        for link in allLinks:
            link = link.get('href')
            if '#' in link:
                link = link.split('#')[0]
            if (link[0:6] == '/wiki/') and (not link[6:11] == 'Talk:') and ('cite_note' not in link) and (not link[6:15] == 'Category:') and (not link[6:15] == 'Template:') and (not link[6:11] == 'File:') and (not link[6:16] == 'Wikipedia:') and (not link[6:11] == 'Help:') and (not link[6:15] == 'Special:'):
                link = 'http://en.wikipedia.org' + str(link)
                link = wikiPage(link, self)
                children.append(link)
        return children

    def get_path(self):
        path = []
        current = self
        while current is not None:
            path = [current.state] + path
            current = current.parent
        return path

def search(start, goalTest):
    if goalTest(start.state):
        return [start.state]
    agenda = []
    agenda.append(start)
    visited = {start.state}
    while not len(agenda) == 0:
        parent = agenda.pop(0)
        for child in parent.get_children():
            if goalTest(child.state):
                return child.get_path()
            elif child.state not in visited:
                visited.add(child.state)
                agenda.append(child)
    return None

goalTest = lambda url: url == goal

###

start = 'http://en.wikipedia.org/wiki/Nepal'
goal  = 'http://en.wikipedia.org/wiki/Cabinet_(government)'

start = wikiPage(start, None)
print search(start, goalTest)




