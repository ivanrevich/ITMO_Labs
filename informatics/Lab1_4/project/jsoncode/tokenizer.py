

class JSONTokenizer:
    def __init__(self, path2file:str, encoding:str="UTF-8"):
        self.path2file = path2file
        self.encoding = encoding
        self.tokens = []
        self.syntax = {
            '"':"DOUBLEQUOTE",
            "'":"QUOTE",
            ' ':"WHITESPACE", 
            '\t':"TAB",
            '\b':"BACKSPACE",
            '\n':"NEWLINE",
            '\r':"CARRIAGERETURN",
            '[':"LEFTBRACKET",
            ']':"RIGHTBRACKET",
            '{':"LEFTBRACE",
            '}':"RIGHTBRACE",
            ':':"COLON",
            ',':"COMMA"
        }
        self.reverse_syntax=dict(zip(self.syntax.values(), self.syntax.keys()))
    
    def tokenize(self):
        text = ""
        with open(self.path2file, encoding=self.encoding) as f:
            text = "".join(f.readlines())
        for el in text:
            if el in self.syntax.keys():
                self.tokens.append(self.syntax[el])
            else:
                self.tokens.append(el)
        return self.tokens