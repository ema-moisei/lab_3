"""4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as
name-parameters. Build and return a string that represents the corresponding XML element.
Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>" """

# cu "\" sau fara?, spatiile?


def build_xml_element(tag, content, **kwargs):
    xml_element = "<"
    xml_element += tag + " "
    for key in kwargs:
        xml_element = xml_element + str(key) + "=\"" + kwargs[key] + "\""
    xml_element = xml_element + ">" + content + "</" + tag + ">"

    return xml_element


def main():

    xml_element = build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid ")
    print(xml_element, "xml_element")


if __name__ == "__main__":
    main()


