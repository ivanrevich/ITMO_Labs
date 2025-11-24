import json
from dicttoxml import dicttoxml
import configparser

data = None

with open("project/usingstdlibs/input.json", 'r', encoding="utf-8") as f:
    data = json.loads("".join(f.readlines()))

xml = dicttoxml(data, attr_type=True)

with open("project/usingstdlibs/output.xml", 'w+', encoding="utf-8") as f:
    f.write(xml.decode("utf-8"))




config = configparser.ConfigParser()

def convertJsonToIni(jsonData, config=None, parentSection=None):
    if config is None:
        config = configparser.ConfigParser()
    
    if isinstance(jsonData, dict):
        for key, value in jsonData.items():
            currentSection = parentSection + '.' + key if parentSection else key
            
            if isinstance(value, dict):
                config.add_section(currentSection)
                convertJsonToIni(value, config, currentSection)
            elif isinstance(value, list):
                config.add_section(currentSection)
                for i, item in enumerate(value):
                    config.set(currentSection, f'item_{i}', str(item).replace("True", "true").replace("False", "false").replace("None", "null"))
            else:
                if parentSection:
                    if not config.has_section(parentSection):
                        config.add_section(parentSection)
                    config.set(parentSection, key, str(value))
                else:
                    if not config.has_section('main'):
                        config.add_section('main')
                    config.set('main', key, str(value))
    
    return config


config = convertJsonToIni(data)
with open("project/usingstdlibs/output.ini", "w+", encoding="utf-8") as f:
    config.write(f)

