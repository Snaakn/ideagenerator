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

    """ def test_add_new_library_element_entry(self):
        lib = Library()
        lib.addElem("test") """


if __name__ == '__main__':
    unittest.main()