# XML is a markup language designed for storing and transporting data with a focus on hierarchical structures.
# xml.etree.ElementTree, lxml, xml.dom.minidom - Several libraries for working with XML
# Writing to an XML file
import xml.etree.ElementTree as ET

root = ET.Element('root')
child1 = ET.SubElement(root, 'child1')
child1.text = 'This is child 1'

child2 = ET.SubElement(root, 'child2', attrib={'name': 'second'})
child2.text = 'This is child 2'
# Save to file
tree = ET.ElementTree(root)
tree.write('output.xml')

