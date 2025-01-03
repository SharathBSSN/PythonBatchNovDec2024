"""
Purpose: Reading(Parsing) XML
"""

import xml.etree.ElementTree as ET
from pprint import pp

xml_tree = ET.parse("books.xml")

# print(dir(xml_tree))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_root', '_setroot', 'find', 'findall', 'findtext', 'getroot', 'iter', 'iterfind', 'parse', 'write', 'write_c14n']

# # To find a tag
# print(xml_tree.find('book'))
# print(xml_tree.findall('book'))
# print()

"""
ref:
<catalog>
    <book isbn="0-596-00128-2">
        <title>Python &amp; XML</title>
        <date>December 2001</date>
        <author>Jones, Drake</author>
    </book>
</catalog>
"""

books = {}

for ech_bk in xml_tree.findall('book'):
    isbn = ech_bk.attrib['isbn']
    title = ech_bk.find('title'). text
    # print(isbn)
    # print(title)
    books[isbn] = title
    
pp(books)