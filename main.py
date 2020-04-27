#!/usr/bin/env python

from dictionary import Library, Generator

def main():
    lib = Library()
    gen = Generator()
    
    #add Genres
    g = "Genre"
    lib.add(g, "Shooter")
    lib.add(g, "RPG")
    lib.add(g, "Point and Click Adventure")
    lib.add(g, "Adventure")
    lib.add(g, "Sports")
    lib.add(g, "Racing")

    #add actions
    a = "Action"
    lib.add(a, "shoot")
    lib.add(a,"sort")
    lib.add(a,"avoid")
    lib.add(a,"buy")
    lib.add(a,"sell")
    
    
    #add Objects
    o = "Objects"
    lib.add(o, "Birds")
    lib.add(o, "Bottles")
    lib.add(o, "Holes")
    lib.add(o, "Walls")
    lib.add(o, "Drugs")
    lib.add(o, "the Cops")
    lib.add(o, "angry Wikings")

    # add patterns
    gen.add("A #Genre game where you #Action #Objects")
    gen.add("A #Genre Game about #Objects . But be careful of #Objects !")
    gen.add("A #Genre #Genre Mix with #Objects")



    result = gen.generate(lib)
    print(result)

if __name__ == "__main__":
    main()