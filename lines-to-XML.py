import xml.etree.ElementTree as ET

def main(): 
    input_string = "P|Carl Gustaf|Bernadotte\nT|0768-101801|08-101801"
    file_name = "output.xml"

    formatted_string = input_string.splitlines()
    # list_items = []
    xml = ET.Element("people")
    person = ET.SubElement(xml, "person")

    for items in formatted_string: 
        sep_string = items.split(sep = "|")
        if sep_string[0] == "P": 
           firstname = ET.SubElement(person, "firstname")
           firstname.text = sep_string[1]
           lastname = ET.SubElement(person, "lastname")
           lastname.text = sep_string[2]
        elif sep_string[0] == "T":
            phone = ET.SubElement(person, "phone")
            mobile = ET.SubElement(phone, "mobile")
            mobile.text = sep_string[1]
            telephone = ET.SubElement(phone, "telephone")
            telephone.text = sep_string[2]

        # list_items.append(sep_string)
        # formatted_list = list(list_items)

    
    xmlTree = ET.ElementTree(element=xml)
    ET.indent(xml, space="\t", level=0)
    xmlTree.write(file_name, encoding="utf-8")

if __name__ == "__main__":
    main()