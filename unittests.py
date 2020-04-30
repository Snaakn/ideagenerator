#!/usr/bin/env python

from dictionary import Library, Generator
import unittest


class ideaGeneratorTest(unittest.TestCase):
    def test_add_new_library_element(self):
        lib = Library()
        old_count = lib.elem_count()
        lib.add_element("testElement")
        self.assertNotEqual(old_count, lib.elem_count())
    
    def test_get_library_element_by_name(self):
        lib = Library()
        test_elem_name = "test"
        lib.add_element(test_elem_name)
        self.assertEqual(test_elem_name, lib.get_element_by_name(test_elem_name).get_name())

    # add an entry to a library element
    def test_add_new_library_element_entry(self):
        lib = Library()
        test_name = "test"
        lib.add_element(test_name)
        before_count = lib.get_element_by_name(test_name).entry_count()
        lib.get_element_by_name(test_name).add_entry("Testentry")
        self.assertNotEqual(before_count, lib.get_element_by_name(test_name).entry_count)
    
    # new add function adds elements and entries if an element already exists it only adds the entry to it
    def test_add_element_with_entry(self):
        lib = Library()
        test_name = "Genre"
        test_genre = "Shooter"
        
        lib.add_element(test_name)
        before_count = lib.elem_count()
        # function to test
        lib.add(test_name, test_genre)
        self.assertEqual(before_count, lib.elem_count())
    
    def test_generate_text(self):
        lib = Library()
        test_genre = "Shooter"
        lib.add("Genre", test_genre)
        result = lib.get_element_by_name("Genre").generate()
        self.assertEqual(test_genre, result)

    def tes_generate_simple_phrase(self):
        lib = Library()
        lib.add("Genre", "Shooter")
        gen = Generator()
        gen.add("A #Genre Game") 
        result = gen.generate(lib)
        self.assertEquals("A Shooter Game ", result)


if __name__ == '__main__':
    unittest.main()