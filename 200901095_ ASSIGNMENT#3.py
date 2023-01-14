
import xml.etree.ElementTree as ET
from prettytable import PrettyTable

# parse the xml file
tree = ET.parse('compiler.xml')
root = tree.getroot()

# create a table to hold the data
table = PrettyTable()


# add columns to the table
print("THE INFORMATION IS \n")
table.field_names = [ 'BOOK_ID','AUTHOR', 'TITLE','GENRE', 'PRICE','PUBLISH_DATE', 'DESCRIPTION']

# iterate through the xml elements and add them to the table
for child in root:
    table.add_row([child.get("id"),child.find("author").text,child.find("title").text,
                   child.find("genre").text,child.find("price").text,
                   child.find("publish_date").text,
                   child.find("description").text])

# print the table
print(table)


