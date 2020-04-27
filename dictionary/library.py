from dictionary import Element


class Library:
    elemList = []
    def __init__(self):
        print("Element added")

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
    
