"""
Purpose: writing an XML file
    XML - eXtensible Markup Language
        - designed to store and transport data.
        - often used for distributing data over the
           Internet(especial in web development).

XML vs HTML
    XML : is used to store or transport data. So the XML is a Complement to HTML.
    HTML: is used to format and display the same data.

- XML Tags are Case Sensitive
- All XML Elements Must Have a Closeing Tag
    <p>This is a paragraph.</p>
    <br />  <!-- This is a self closing -->
- XML Attribute Values Must Always be Quoted

"""

import xml.etree.ElementTree as ET
from xml.dom import minidom


"""
mport xml
print(dir(xml))
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']


print(dir(ET)):
['C14NWriterTarget', 'Comment', 'Element', 'ElementPath', 'ElementTree', 'HTML_EMPTY', 'PI', 'ParseError', 'ProcessingInstruction', 'QName', 'SubElement', 'TreeBuilder', 'VERSION', 'XML', 'XMLID', 'XMLParser', 'XMLPullParser', '_Element_Py', '_ListDataStream', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_escape_attrib', '_escape_attrib_c14n', '_escape_attrib_html', '_escape_cdata', '_escape_cdata_c14n', '_get_writer', '_looks_like_prefix_name', '_namespace_map', '_namespaces', '_raise_serialization_error', '_serialize', '_serialize_html', '_serialize_text', '_serialize_xml', '_set_factories', 'canonicalize', 'collections', 'contextlib', 'dump', 'fromstring', 'fromstringlist', 'indent', 'io', 'iselement', 'iterparse', 'parse', 're', 'register_namespace', 'sys', 'tostring', 'tostringlist', 'warnings', 'weakref']
"""

#creating an xml
root = ET.Element("root")
root.attrib = {"attribute": "test_attrib"}

child = ET.SubElement(root,"child")
sub_child = ET.SubElement(child,"sub_child")
sub_child.text = "sub_child_text"

# To display the xml string
result_str = ET.tostring(root)
print(result_str) # b'<root attribute="test_attrib"><child><sub_child>sub_child_text</sub_child></child></root>
print()


result_str = minidom.parseString(result_str).toprettyxml()
print(result_str) 
# <?xml version="1.0" ?>
# <root attribute="test_attrib">
#         <child>
#                 <sub_child>sub_child_text</sub_child>
#         </child>
# </root>
