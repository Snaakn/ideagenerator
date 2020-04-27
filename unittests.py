#!/usr/bin/env python

from dictionary import Library
import unittest

class ideaGeneratorTest(unittest.TestCase):
    def test_add_new_library_element(self):
        lib = Library()
        oldCount = lib.elemCount()
        lib.addElem("testElement")
        self.assertNotEqual(oldCount, lib.elemCount())
    
    def test_get_library_element_by_name(self):
        lib = Library()
        testElemName = "test"
        lib.addElem(testElemName)
        self.assertEqual(testElemName, lib.getElemByName(testElemName).getName())

    #add an entry to a library element
    def test_add_new_library_element_entry(self):
        lib = Library()
        testName = "test"
        lib.addElem(testName)
        beforeCount = lib.getElemByName(testName).entryCount()
        lib.getElemByName(testName).addEntry("Testentry")
        self.assertNotEqual( beforeCount,lib.getElemByName(testName).entryCount)
    
    # new add function adds elements and entries if an element already exists it only adds the entry to it
    def test_add_element_with_entry(self):
        lib = Library()
        testName = "Genre"
        testGenre = "Shooter"
        
        lib.addElem(testName)
        beforeCount = lib.elemCount()
        # function to test
        lib.add(testName, testGenre)
        self.assertEqual(beforeCount, lib.elemCount())
    
    def test_generate_text(self):
        lib = Library()
        testGenre = "Shooter"
        lib.add("Genre", testGenre)
        result = lib.getElemByName("Genre").generate()
        self.assertEqual(testGenre, result)



if __name__ == '__main__':
    unittest.main()