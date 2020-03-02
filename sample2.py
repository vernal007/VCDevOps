from lxml import etree as ET

#Get the XML file data
stream = open('text.xml','r')

#Parse the data into ElementTree object
xml = ET.parse(stream)

#Get the 'root' Element object from the ElemenTree
root = xml.getroot()

#Iterate through each child of the root Element
for e in root:
    #print the stringfield version of element
    print(ET.tostring(e))
    print("")

    #Print the "Id" attribute of the Element object
    print(e.get("id"))