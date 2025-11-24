from jsoncode.tokenizer import JSONTokenizer
from jsoncode.parser import JSONParser

from INI.INIgenerator import INIGenerator
from XML.XMLgenerator import XMLGenerator

from common.serializer import Serializer
from common.deserializer import Deserializer


tokenizer = JSONTokenizer("project\input.json")
tokens = tokenizer.tokenize()

parser = JSONParser(tokens, "project\\files\\tree.txt")
tree = parser.parse()
parser.save()


serializer = Serializer(tree, "project\\files\\bin.txt")
binData = serializer.JSONSerialize()
serializer.save()


deserializer = Deserializer(binData)
deserializedData = deserializer.deserialize()


iniGen = INIGenerator("project\\files\\output.ini")
iniGen.deserialize2ini(deserializedData)
iniGen.save()

xmlGen = XMLGenerator("project\\files\\output.xml")
xmlGen.deserialize2xml(deserializedData)
xmlGen.save()
