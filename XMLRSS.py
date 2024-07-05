'''try:
    from io import BytesIO as StringIO
except ImportError:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

try:
    from itertools import izip as zip
except ImportError:
    pass

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
'''

from urllib.request import urlopen
from io import BytesIO as StringIO
from xml.etree import ElementTree

#g = urlopen('https://timesofindia.indiatimes.com/rssfeedstopstories.cms')
g = urlopen('https://www.news18.com/rss/tech.xml')
f=StringIO(g.read())
g.close()
tree=ElementTree.parse(f)
f.close()

def topnews(count=5):
    pair = [None,None]
    for elmt in tree.getiterator():
        if elmt.tag=='title':
            #skip=elmt.text.startswith('Top stories')
            skip = elmt.text.startswith('Top news')
            if skip:
                continue
            pair[0]=elmt.text
            if elmt.tag=='title':
                if skip:
                    continue
                pair[1]=elmt.text
                if pair[0] and pair[1]:
                    count-=1
                    yield(pair[0])
                    if not count:
                        return
                    pair=[None,None]

for news in topnews():
    print(news)
