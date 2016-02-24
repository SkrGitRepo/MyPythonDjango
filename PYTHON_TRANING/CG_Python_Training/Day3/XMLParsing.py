#Parsing an xml using Python XML parsing module
import xml.etree.ElementTree as ET

tree = ET.parse('Book.xml')
root = tree.getroot()


print root.tag
print root.attrib

for child in root:
    print child.tag, child.attrib
print root[0].text
print root[0][0].text
print root[0][1].text

for book_id in root.iter('book'):
    print book_id.attrib
    
for book in root.findall('book'):
    author=book.find('author').text
    title=book.find('title').text
    #title=book.get('title')
    print "AUTHOR:",author,"::BOOK TITLE:",title

#writing xml to a new xml file
tree.write('book_output.xml')

'''for book_description in root.iter('description'):
    price = book_description.get()
    print price
    '''
    
    
    





