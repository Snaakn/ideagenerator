from dictionary import Element


class Library:
    lib_count = 0
    def __init__(self):
        self.lib_count += 1
        self.elements = []
        # print("Library created")

    def __del__(self):
        self.lib_count -= 1
        self.elements.clear()

    def add(self, name, entry):
        # if element is already existent add entry to it and return
        for elem in self.elements:
            if name == elem.name:
                elem.add_entry(entry)
                return
        # if not existent create new element and add entry to it
        self.add_element(name)
        self.get_element_by_name(name).add_entry(entry)

    def add_element(self, name):
        self.elements.append(Element(name))
        
    def elem_count(self):
        return len(self.elements)
        
    def get_element_by_name(self, elemName):
        for elem in self.elements:
            if elem.get_name() == elemName:
                return elem
        print("Element not found")
        return Element("")

