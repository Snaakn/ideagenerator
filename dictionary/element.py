from random import Random

class Element:
    def __init__(self, val):
        self.entries = []
        self.name = val
    
    def __del__(self):
        self.entries.clear()
    
    def add_entry(self, entry):
        self.entries.append(entry)
        # print("Added " + entry + " to " + self.name)

    def get_name(self):
        return self.name

    def entry_count(self):
        return len(self.entries)
    
    def generate(self):
        rn = Random()
        rn.seed(a=None, version=2)
        return rn.choice(self.entries)
