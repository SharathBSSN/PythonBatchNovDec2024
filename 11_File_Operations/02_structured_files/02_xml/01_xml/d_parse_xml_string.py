"""
Purpose: To parse(read) xml string
"""

import xml.etree.ElementTree as ET

input_string = """
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Udhay</name>
        </user>
        <user x="3">
            <id>009</id>
            <name>Prakash</name>
        </user>
    </users>
    <users>
        <user x="7">
            <id>002</id>
            <name>Sharath</name>
        </user>
        <user x="9">
            <id>008</id>
            <name>Banoth</name>
        </user>
    </users>
</stuff>
"""

stuff_tree = ET.fromstring(input_string)

# print(dir(stuff_tree))
# ['__bool__', '__class__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'attrib', 'clear', 'extend', 'find', 'findall', 'findtext', 'get', 'insert', 'items', 'iter', 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 'set', 'tag', 'tail', 'text']

nodes = stuff_tree.find("users")
# print(nodes)
# <Element 'users' at 0x7db08b246980>
# print(dir(nodes))
# ['__bool__', '__class__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'attrib', 'clear', 'extend', 'find', 'findall', 'findtext', 'get', 'insert', 'items', 'iter', 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 'set', 'tag', 'tail', 'text']

nodes = stuff_tree.findall("users")
# print(nodes)
# [<Element 'users' at 0x7cf5ff0de980>, <Element 'users' at 0x7cf5ff0debb0>]

nodes = stuff_tree.findall("user")
# print(nodes)
# [] NOTE: No Elements founf

nodes = stuff_tree.findall("users/user")
print(nodes)
# [<Element 'user' at 0x7807b3cea980>, <Element 'user' at 0x7807b3ceaa70>, <Element 'user' at 0x7807b3ceabb0>, <Element 'user' at 0x7807b3ceaca0>]

for item in nodes:
    print("\nName", item.find("name").text)
    print("Id", item.find("id").text)
    print("Attribute", item.get("x"))

"""
result:
    Name Udhay
    Id 001
    Attribute 2

    Name Prakash
    Id 009
    Attribute 3

    Name Sharath
    Id 002
    Attribute 7

    Name Banoth
    Id 008
    Attribute 9
"""