from dictionary import Element


class Library:
    libCount = 0
    def __init__(self):
        self.elemList = []
        print("Library created")

    def __del__(self):
        self.elemList.clear()

    def add(self, name, entry):
        # if element is already existent add entry to it and return
        for elem in self.elemList:
            if name == elem.name:
                elem.addEntry(entry)
                return
        # if not existent create new element and add entry to it
        self.addElem(name)
        self.getElemByName(name).addEntry(entry)


    def addElem(self, name):
        self.elemList.append(Element(name))
        
    def elemCount(self):
        return len(self.elemList)
        
    def getElemByName(self, elemName):
        for elem in self.elemList:
            if elem.getName() == elemName:
                return elem
        print("Element not found")
        return Element("")
    
