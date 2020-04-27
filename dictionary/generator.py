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
        return self.parsePattern(rn.choice(self.patterns), lib)

    def parsePattern(self , pattern, lib):
        words = pattern.split()
        result = ""
        for word in words:
            if word[0] == '#':
                word = lib.getElemByName(word.replace('#', '')).generate()
            result += word + " "
        return result