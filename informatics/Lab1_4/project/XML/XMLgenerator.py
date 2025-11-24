class XMLGenerator:
    def __init__(self, path2outfile:str, encoding="UTF-8"):
        self.path2outfile=path2outfile
        self.encoding = encoding
        self.out = None
        self.idx = 0
        
    def dict2xml(self, data:dict, up=""):
        xml_lines = []
        for key, value in data.items():
            if isinstance(value, dict):
                xml_lines.append(f"{up}<{key}>")
                xml_lines.extend(self.dict2xml(value, up+"\t"))
                xml_lines.append(f"{up}</{key}>")
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        xml_lines.append(f"{up}<{key}>")
                        xml_lines.extend(self.dict2xml(item, up+"\t"))
                        xml_lines.append(f"{up}</{key}>")
                    else:
                        xml_lines.append(f"{up}<{key}>{item}</{key}>")
            else:
                xml_lines.append(f"{up}<{key}>{value}</{key}>")
        return xml_lines


    def deserialize2xml(self, data):
        if data is None: return ""
        if isinstance(data, dict):
            xml_lines = self.dict2xml(data)
        else:
            xml_lines = [f"data = {data}"]
        
        xml_lines.insert(0, f'<?xml version="1.0" encoding="{self.encoding}" ?>')
        self.out = "\n".join(xml_lines)
        return self.out


    def save(self):
        if self.out==None:
            raise Exception("Output data is None")
        with open(self.path2outfile, "w+", encoding=self.encoding) as f:
            f.write(self.out)