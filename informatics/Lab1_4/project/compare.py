import time
from jsoncode.tokenizer import JSONTokenizer
from jsoncode.parser import JSONParser

from INI.INIgenerator import INIGenerator
from XML.XMLgenerator import XMLGenerator

import gc

from common.serializer import Serializer
from common.deserializer import Deserializer
import json
from dicttoxml import dicttoxml
import configparser
import pickle



def myini():
    a = time.process_time_ns()
    tokenizer = JSONTokenizer("project\input.json")
    tokens = tokenizer.tokenize()

    parser = JSONParser(tokens, "project\\files\\tree.txt")
    tree = parser.parse()


    serializer = Serializer(tree, "project\\files\\bin.txt")
    binData = serializer.JSONSerialize()


    deserializer = Deserializer(binData)
    deserializedData = deserializer.deserialize()


    iniGen = INIGenerator("project\\files\\output.ini")
    iniGen.deserialize2ini(deserializedData)
    return time.process_time_ns()-a

def myxml():
    a = time.process_time_ns()

    tokenizer = JSONTokenizer("project\input.json")
    tokens = tokenizer.tokenize()

    parser = JSONParser(tokens, "project\\files\\tree.txt")
    tree = parser.parse()


    serializer = Serializer(tree, "project\\files\\bin.txt")
    binData = serializer.JSONSerialize()


    deserializer = Deserializer(binData)
    deserializedData = deserializer.deserialize()

    xmlGen = XMLGenerator("project\\files\\output.xml")
    xmlGen.deserialize2xml(deserializedData)
    return time.process_time_ns()-a


def nomyxml():
    a = time.process_time_ns()
    datajs = None

    with open("project/input.json", 'r', encoding="utf-8") as f:
        datajs = json.loads("".join(f.readlines()))


    with open("project/bin.pkl", 'wb+') as f:
        pickle.dump(datajs, f)

    with open("project/bin.pkl", "rb") as f:
        data = pickle.load(f)


    xml = dicttoxml(data, attr_type=True)

    return time.process_time_ns()-a



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

def nomyini():
    a = time.process_time_ns()
    datajs = None

    with open("project/input.json", 'r', encoding="utf-8") as f:
        datajs = json.loads("".join(f.readlines()))

    with open("project/bin2.pkl", 'wb+') as f:
        pickle.dump(datajs, f)

    with open("project/bin2.pkl", "rb") as f:
        data = pickle.load(f)
        
    config = configparser.ConfigParser()
    config = convertJsonToIni(data)
    return time.process_time_ns()-a


my_xml_time_ns = sum([myxml() for i in range(100)])//100
gc.collect()
my_ini_time_ns = sum([myini() for i in range(100)])//100
gc.collect()

gc.collect()
nomy_ini_time_ns = sum([nomyini() for i in range(100)])//100
gc.collect()
nomy_xml_time_ns = sum([nomyxml() for i in range(100)])//100
gc.collect()

print("My ini time:", my_ini_time_ns, "ns")
print("Not my ini time:", nomy_ini_time_ns, "ns")
print(my_ini_time_ns/nomy_ini_time_ns)
print()
print("My xml time:", my_xml_time_ns, "ns")
print("No my xml time:", nomy_xml_time_ns, "ns")
print(my_xml_time_ns/nomy_xml_time_ns)