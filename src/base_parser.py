class BaseParser:
    def __init__(self, vuln_name, pattern):
        self.vuln_name = "base vulnerable"
        self.pattern = pattern
    
    def parse(self, cpp_code):
        pass

