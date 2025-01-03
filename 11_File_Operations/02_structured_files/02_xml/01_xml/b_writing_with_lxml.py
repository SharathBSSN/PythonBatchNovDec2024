"""
Purpose: write xml file using lxml module
"""
try:
    from lxml import etree
except ModuleNotFoundError as ex:
    print(repr(ex))
    from os import system

    system("pip install lxml")
    from lxml import etreeree


#creating an xml elements
root = etree.Element("root")
child = etree.Element("child")
sub_child = etree.Element("sub_child")
sub_child.text = "sub_child"

#creating a xml tree
root.append(child)
child.append(sub_child)

result_str = etree.tostring(root)
print(result_str) # b'<root><child><sub_child>sub_child</sub_child></child></root>'
print()

result_str = etree.tostring(root, pretty_print=True)
print(result_str)
# b'<root>\n  <child>\n    <sub_child>sub_child</sub_child>\n  </child>\n</root>\n'
print()
print(result_str.decode("utf-8"))
# <root>
#   <child>
#     <sub_child>sub_child</sub_child>
#   </child>
# </root>