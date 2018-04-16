import utils
import base_parser
import collections
import re


class FormatStringParser(base_parser.BaseParser): 
    def __init__(self):
        self.output = []
        self.vuln_name = 'Format String'
        self.pattern = [r'(printf[(][a-zA-Z0-9_]*)([)])'] # TODO: improve to parse cases with whitespaces, maybe find another regex for this vuln
    
    def parse(self, cpp_code):
        line_counter = 0
        for line in cpp_code:
            line_counter += 1
             
            matches = re.finditer(self.pattern[0], line, re.IGNORECASE)
            for matchNum, match in enumerate(matches):
                matchNum = matchNum + 1
                self.output.append(base_parser.warning(line_counter, str(line), self.vuln_name, 'CRITICAL', 'Possible format string vulnerable'))
            
        return self.output
            
