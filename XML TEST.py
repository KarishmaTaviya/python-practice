import xml
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom.minidom import parseString

BOOKs = {
    '1':{'Title':'Core Python','Edition':2,'Year':2007},
    '2':{'Title':'Python prog','Edition':5,'Year':2011},
}
books = Element('books')
for isbn,info in BOOKs.items():
    book = SubElement(books,'book')
    for key,val in info.items():
        SubElement(book,key).text=','.join(str(val).split(':'))

xml=tostring(books)
print('**** Raw XML ****')
print(xml)

print('\n** PRETTY PRINTED XML **')
dom=parseString(xml)
print(dom.toprettyxml(' '))

print('**** Flat Structure *****')
for elmt in books.getiterator():
    print(elmt.tag, '-', elmt.text)

print('*** Titles only ****')
for book in books.findall('.//Title'):
    print(book.text)