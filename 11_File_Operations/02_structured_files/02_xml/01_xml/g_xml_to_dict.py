"""
Purpose: XML to python DICT conversion
"""
try:
    import xmltodict
    from pprint import pp
except ModuleNotFoundError as ex:
    print(repr(ex))
    from os import system

    system("pip install xmltodict")
    import xmltodict
    from pprint import pp


# with open("books.xml", "r") as fh:
#     file_content = fh.read()

# # print(file_content) # ----? XML STring

# xml_dict = xmltodict.parse(file_content)
# # pp(xml_dict)

# books = {}

# for ech_bk in xml_dict['catalog']['book']:
#     isbn = ech_bk['@isbn']
#     title = ech_bk['title']
#     books[isbn] = title

# pp(books)

# Assignment:  explore how to convert the dict ,
# back to xml using this xmltodict module.. Hint: unparse()

xml_dict ={'catalog': {'book': [{'@isbn': '0-596-00128-2',
                       'title': 'Python & XML',
                       'date': 'December 2001',
                       'author': 'Jones, Drake'},
                      {'@isbn': '0-596-15810-6',
                       'title': 'Programming Python, 4th Edition',
                       'date': 'October 2010',
                       'author': 'Lutz'},
                      {'@isbn': '0-596-15806-8',
                       'title': 'Learning Python, 4th Edition',
                       'date': 'September 2009',
                       'author': 'Lutz'},
                      {'@isbn': '0-596-15808-4',
                       'title': 'Python Pocket Reference, 4th Edition',
                       'date': 'October 2009',
                       'author': 'Lutz'},
                      {'@isbn': '0-596-00797-3',
                       'title': 'Python Cookbook, 2nd Edition',
                       'date': 'March 2005',
                       'author': 'Martelli, Ravenscroft, Ascher'},
                      {'@isbn': '0-596-10046-9',
                       'title': 'Python in a Nutshell, 2nd Edition',
                       'date': 'July 2006',
                       'author': 'Martelli'}]}}
                       


# print(xmltodict.unparse(xml_dict))

with open ("dict_to_xml.xml", "w") as fh:
    fh.write(xmltodict.unparse(xml_dict))