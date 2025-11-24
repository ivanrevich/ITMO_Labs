class Serializer:
    def __init__(self, tree, path2BinResFile:str="bin.txt", encoding="UTF-8"):
        self.path2BinResFile=path2BinResFile
        self.encoding = encoding
        self.tree = tree
        self.out = None

    def serialize(self, data):
        if isinstance(data, dict):
            binary = b'\x01' + len(data).to_bytes(4, 'big')
            for k, v in data.items():
                binary += self.serialize(k) + self.serialize(v)
            return binary
        
        elif isinstance(data, str):
            encoded = data.encode('UTF-8')
            return b'\x02' + len(encoded).to_bytes(4, 'big') + encoded
        
        elif isinstance(data, (list, tuple)):
            binary = b'\x03' + len(data).to_bytes(4, 'big')
            for item in data:
                binary += self.serialize(item)
            return binary
        
        elif isinstance(data, int):
            return b'\x04' + data.to_bytes(8, 'big', signed=True)
        
        elif isinstance(data, float):
            return b'\x05' + int(data).to_bytes(8, 'big', signed=True)+int((data%1)*10000000000000000).to_bytes(8, 'big', signed=True)
        
        elif data is True or data is False:
            return b'\x06' + data.to_bytes(1, "little", signed=True)
        elif data is None:
            return b'\x07'
        
    def JSONSerialize(self):
        self.out = self.serialize(self.tree)
        return self.out
    
    
    def save(self):
        if self.out==None:
            raise Exception("Output data is None")
        with open(self.path2BinResFile, "w+", encoding=self.encoding) as f:
            f.write(str(self.out))