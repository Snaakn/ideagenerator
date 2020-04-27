from random import Random

class Element:
    def __init__(self, val):
        self.entries = []
        self.name = val
    
    def __del__(self):
        self.entries.clear()
    
    def addEntry(self, entry):
        self.entries.append(entry)
        print("Added " + entry + " to " + self.name)

    def getName(self):
        return self.name

    def entryCount(self):
        return len(self.entries)
    
    def generate(self):
        rn = Random()
        rn.seed(a=None, version=2)
        text = rn.choice(self.entries)
        return text