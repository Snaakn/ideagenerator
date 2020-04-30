from dictionary import Library
from random import Random

class Generator:

    def __init__(self):
        self.patterns = []

    def add(self, pattern):
        self.patterns.append(pattern)
    
    def generate(self, lib):
        rn = Random()
        rn.seed(a=None, version=2)
        return self.parse_pattern(rn.choice(self.patterns), lib)

    def parse_pattern(self, pattern, lib):
        words = pattern.split()
        result = ""
        for word in words:
            if word[0] == '#':
                word = lib.get_element_by_name(word.replace('#', '')).generate()
            result += word + " "
        return result
