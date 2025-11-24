class INIGenerator:
    def __init__(self, path2file:str, encoding="UTF-8"):
        self.idx = 0
        self.encoding = encoding
        self.type_markers = {
            0x01: "struct",
            0x02: "str", 
            0x03: "array",
            0x04: "int",
            0x05: "float",
            0x06: "bool",
            0x07: "null"
        }
        self.out = None
        self.path2file = path2file
    
    def dict2ini(self, data:dict, section_prefix=""):
        ini_lines = []
        
        for key, value in data.items():
            if isinstance(value, dict):
                section_name = f"{section_prefix}{key}" if section_prefix else key
                ini_lines.append(f"[{section_name}]")
                ini_lines.extend(self.dict2ini(value, f"{section_name}."))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        section_name = f"{section_prefix}{key}.{i}" if section_prefix else f"{key}.{i}"
                        ini_lines.append(f"[{section_name}]")
                        ini_lines.extend(self.dict2ini(item, ""))
                    else:
                        ini_lines.append(f"{key}.{i} = {item}")
            else:
                ini_lines.append(f"{key} = {value}")
        
        return ini_lines
    
    def deserialize2ini(self, data):
        if data is None: return ""
        
        if isinstance(data, dict):
            ini_lines = self.dict2ini(data)
        else:
            ini_lines = [f"data = {data}"]
        self.out = ("\n".join(ini_lines)).replace("True", "true").replace("False", "false").replace("None", "null")
        return self.out
    
    def save(self):
        if self.out==None:
            raise Exception("Output data is None")
        with open(self.path2file, "w+", encoding=self.encoding) as f:
            f.write(str(self.out))


