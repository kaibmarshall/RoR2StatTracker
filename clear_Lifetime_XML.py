import xml.etree.ElementTree as ET

#parse XMLs and get root elements

Life_Totals_XML = ET.parse("LifetimeTotals.xml")
Life_Totals_XML_root = Life_Totals_XML.getroot()




for element in Life_Totals_XML_root.iter():
    if element.tag == "Stats":
        continue
    elif element.tag == "survivorCounts":
        continue
    else:
       # print(element)
        element.text = "0"

Life_Totals_XML.write('LifetimeTotals.xml')