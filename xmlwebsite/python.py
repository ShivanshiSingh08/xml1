from lxml import etree

# Load the XSD schema
xsd_schema = etree.XMLSchema(etree.parse('product.xsd'))

# Load and parse the XML instance
xml_instance = etree.parse('products.xml')

# Validate the XML instance against the XSD schema
if xsd_schema.validate(xml_instance):
    print("XML is valid against the XSD schema.")
else:
    print("XML is not valid against the XSD schema.")
