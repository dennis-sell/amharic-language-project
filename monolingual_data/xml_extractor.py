from xml.etree import ElementTree as ET

tree = ET.parse('amwiki-20150412-pages-articles.xml')
root = tree.getroot()

URI = "{http://www.mediawiki.org/xml/export-0.10/}"
for page in root:
    for revision in page.findall(URI + "revision"):
        for text in revision.findall(URI + "text"):
            if text.text:
                amharic_text = text.text.encode('utf-8')
                if amharic_text:
                    print amharic_text
