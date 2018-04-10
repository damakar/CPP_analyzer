import collections

warning = collections.namedtuple('Warning', ['line_count', 'line', 'name', 'lvl', 'msg'])

class BaseParser:
    def __init__(self, vuln_name, pattern):
        self.vuln_name = "base vulnerable"
        self.pattern = pattern
        self.output = [] # array of warnings 
    
    def parse(self, cpp_code):
        pass

