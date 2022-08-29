import xml.etree.ElementTree as ET

def main(): 
    input_file = open("input.txt", "r")
    input_string = input_file.read()
    file_name = "output.xml"
    formatted_string = input_string.splitlines()
    xml = ET.Element("people")
    family_state = False

    for items in formatted_string: 
        sep_string = items.split(sep = "|")

        if sep_string[0] == "P":
            family_state = False
            person = ET.SubElement(xml, "person") 
            firstname = ET.SubElement(person, "firstname")
            firstname.text = sep_string[1]
            lastname = ET.SubElement(person, "lastname")
            lastname.text = sep_string[2]

        elif sep_string[0] == "T":
            if family_state == True: 
                phone = ET.SubElement(family, "phone")
            
            if family_state == False: 
                phone = ET.SubElement(person, "phone")
           
            mobile = ET.SubElement(phone, "mobile")
            mobile.text = sep_string[1]
            telephone = ET.SubElement(phone, "telephone")
            telephone.text = sep_string[2]

        elif sep_string[0] == "A": 
            if family_state == True: 
                address = ET.SubElement(family, "address")

            if family_state == False: 
                address = ET.SubElement(person, "address")

            street = ET.SubElement(address, "street")
            street.text = sep_string[1]
            city = ET.SubElement(address, "city")
            city.text = sep_string[2]
            
            if len(sep_string) > 3: 
                postal_number = ET.SubElement(address, "postalnumber")
                postal_number.text = sep_string[3]

        elif sep_string[0] == "F":
            family_state = True
            family = ET.SubElement(person, "family")
            name = ET.SubElement(family, "name")
            name.text = sep_string[1]
            born = ET.SubElement(family, "born")
            born.text = sep_string[2]

# builds xmlTree from element
    xmlTree = ET.ElementTree(element=xml)
# indent properly
    ET.indent(xml, space="\t", level=0)
# write to file
    xmlTree.write(file_name, encoding="utf-8")

if __name__ == "__main__":
    main()