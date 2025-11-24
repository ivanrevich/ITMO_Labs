class Deserializer:
    def __init__(self, binary: bytearray, encoding="UTF-8"):
        self.encoding = encoding
        self.binary = binary
        self.idx = 0
        self.type_markers = {
            0x01: "struct",
            0x02: "str", 
            0x03: "array",
            0x04: "int",
            0x05: "float",
            0x06: "bool",
            0x07: "null"
        }
    
    def readOneByte(self):
        if self.idx >= len(self.binary):
            return None
        byte = self.binary[self.idx]
        self.idx += 1
        return byte
    
    def getBytes(self, length):
        if self.idx + length > len(self.binary):
            raise IndexError(f"Not enough bytes to read {length} bytes")
        data = self.binary[self.idx:self.idx + length]
        self.idx += length
        return data
    
    def readUint32(self):
        data = self.getBytes(4)
        return int.from_bytes(data, "big")
    
    def readInt64(self):
        data = self.getBytes(8)
        return int.from_bytes(data, "big", signed=True)
    
    def deserializeString(self):
        length = self.readUint32()
        string_bytes = self.getBytes(length)
        return string_bytes.decode(self.encoding)
    
    def deserializeInt(self):
        return self.readInt64()
    
    def deserializeFloat(self):
        int_part = self.readInt64()
        frac_part = self.readInt64()
        
        if frac_part < 0:
            value = int_part - abs(frac_part) / 10000000000000000
        else:
            value = int_part + frac_part / 10000000000000000
            
        return value
    
    def deserializeBool(self):
        bool_byte = self.readOneByte()
        return bool(bool_byte)
    
    def deserializeNull(self):
        return None
    
    def deserializeArray(self):
        length = self.readUint32()
        arr = []
        for _ in range(length):
            element = self.deserialize()
            arr.append(element)
        return arr
    
    def deserializeStruct(self):
        length = self.readUint32()
        obj = {}
        for _ in range(length):
            key = self.deserialize()
            value = self.deserialize()
            if not isinstance(key, (str, int)):
                raise TypeError(f"Dictionary key must be string or int, got {type(key)}")
            obj[key] = value
        return obj
    
    def deserialize(self):
        if self.idx >= len(self.binary):
            return None
            
        type_byte = self.readOneByte()
        
        if type_byte in self.type_markers:
            data_type = self.type_markers[type_byte]
            
            if data_type == "struct":
                return self.deserializeStruct()
            elif data_type == "str":
                return self.deserializeString()
            elif data_type == "array":
                return self.deserializeArray()
            elif data_type == "int":
                return self.deserializeInt()
            elif data_type == "float":
                return self.deserializeFloat()
            elif data_type == "bool":
                return self.deserializeBool()
            elif data_type == "null":
                return self.deserializeNull()
        else:
            raise ValueError(f"Unknown type, byte: 0x{type_byte:02x}")
    
    