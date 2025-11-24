class JSONParser:
    def __init__(self, tokens: list[str], path2TreeResFile:str="tree.txt", encoding="UTF-8"):
        self.tokens = tokens
        self.idx = 0
        self.encoding = encoding
        self.path2TreeResFile = path2TreeResFile
        self.syntax = {
            '"': "DOUBLEQUOTE",
            "'": "QUOTE",
            ' ': "WHITESPACE", 
            '\t': "TAB",
            '\b': "BACKSPACE",
            '\n': "NEWLINE",
            '\r': "CARRIAGERETURN",
            '[': "LEFTBRACKET",
            ']': "RIGHTBRACKET",
            '{': "LEFTBRACE",
            '}': "RIGHTBRACE",
            ':': "COLON",
            ',': "COMMA"
        }
        self.dataTree = []
        self.binary = []
        self.reverse_syntax = {v: k for k, v in self.syntax.items()}

    def nowToken(self):
        return self.tokens[self.idx] if self.idx < len(self.tokens) else None

    def skipWhitespace(self):
        while self.idx < len(self.tokens) and self.tokens[self.idx] in ["WHITESPACE", "TAB", "NEWLINE", "CARRIAGERETURN"]:
            self.idx += 1

    def parseNonliteral(self):
        self.skipWhitespace()
        literalChars = []
        while self.idx < len(self.tokens):
            token = self.tokens[self.idx]
            if token in ["COMMA", "RIGHTBRACE", "RIGHTBRACKET", "WHITESPACE", "TAB", "NEWLINE"]:
                break
                
            if token in self.reverse_syntax:
                literalChars.append(self.reverse_syntax[token])
            else:
                literalChars.append(token)
                
            self.idx += 1
        
        literalStr = ''.join(literalChars)

        if literalStr == "true":
            return True
        elif literalStr == "false":
            return False
        elif literalStr == "null":
            return None
        else:
            try:
                if '.' in literalStr or 'e' in literalStr.lower():
                    return float(literalStr)
                else:
                    return int(literalStr)
            except ValueError:
                return literalStr

    def parseString(self):
        quoteType = self.nowToken()
        self.idx += 1
        
        result = []
        while self.idx < len(self.tokens):
            token = self.tokens[self.idx]
            
            if token == quoteType:
                self.idx += 1
                break
            elif token in self.reverse_syntax:
                result.append(self.reverse_syntax[token])
            else:
                result.append(token)
                
            self.idx += 1
        
        return ''.join(result)

    def parseValue(self):
        self.skipWhitespace()
        token = self.nowToken()
        
        if token == "LEFTBRACE":
            return self.parseObject()
        elif token == "LEFTBRACKET":
            return self.parseArray()
        elif token in ["DOUBLEQUOTE", "QUOTE"]:
            return self.parseString()
        else:
            return self.parseNonliteral()

    def parseObject(self):
        self.idx += 1
        self.skipWhitespace()
        
        obj = {}
        if self.nowToken() == "RIGHTBRACE":
            self.idx += 1
            return obj
        
        while self.idx < len(self.tokens):
            key = self.parseString() if self.nowToken() in ["DOUBLEQUOTE", "QUOTE"] else self.parseNonliteral()
            
            self.skipWhitespace()
            
            if self.nowToken() != "COLON":
                break

            self.idx += 1
            self.skipWhitespace()
            
            value = self.parseValue()
            obj[key] = value
            
            self.skipWhitespace()
            
            if self.nowToken() == "RIGHTBRACE":
                self.idx += 1
                break
            elif self.nowToken() == "COMMA":
                self.idx += 1
                self.skipWhitespace()
            else:
                break
        
        return obj

    def parseArray(self):
        self.idx += 1
        self.skipWhitespace()
        
        arr = []

        if self.nowToken() == "RIGHTBRACKET":
            self.idx += 1
            return arr
        
        while self.idx < len(self.tokens):
            value = self.parseValue()
            arr.append(value)
            
            self.skipWhitespace()
            
            if self.nowToken() == "RIGHTBRACKET":
                self.idx += 1
                break
            elif self.nowToken() == "COMMA":
                self.idx += 1
                self.skipWhitespace()
            else:
                break
        
        return arr

    def parse(self):
        self.skipWhitespace()
        return self.parseValue()
    
    def save(self):
        with open(self.path2TreeResFile, "w+", encoding=self.encoding) as f:
            f.write(str(self.dataTree))
        