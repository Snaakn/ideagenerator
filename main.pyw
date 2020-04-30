#!/usr/bin/env python

from dictionary import Library, Generator
import tkinter as tk
from tkinter import filedialog, Text
import os

def generate_text(lib, gen):
    # Finally generate a phrase
    result = gen.generate(lib)
    return(result)

def main():
    lib = Library()
    gen = Generator()
    
    # add Genres
    g = "Genre"
    lib.add(g, "Shooter")
    lib.add(g, "RPG")
    lib.add(g, "Point and Click Adventure")
    lib.add(g, "Adventure")
    lib.add(g, "Sports")
    lib.add(g, "Racing")
    lib.add(g, "Cards")
    lib.add(g, "Exploration")
    lib.add(g, "Simulation")


    # add actions
    a = "Action"
    lib.add(a, "shoot")
    lib.add(a, "sort")
    lib.add(a, "avoid")
    lib.add(a, "buy")
    lib.add(a, "sell")
    lib.add(a, "trade")
    lib.add(a, "beat")
    lib.add(a, "transport")
    lib.add(a, "catch")
    lib.add(a, "")

    
    # add Objects
    o = "Objects"
    lib.add(o, "Birds")
    lib.add(o, "Bottles")
    lib.add(o, "Holes")
    lib.add(o, "Walls")
    lib.add(o, "Drugs")

    # enemies
    e = "Enemies"
    lib.add(e, "the Cops")
    lib.add(e, "angry Wikings")
    lib.add(e, "Aliens")
    lib.add(e, "Gangsters")
    lib.add(e, "Enemies")
    lib.add(e, "Monsters")
    lib.add(e, "Demons")
    lib.add(e, "Climate Change")

    # collectibles
    c = "Collectibles"
    lib.add(c, "Diamonds")
    lib.add(c, "Gold")
    lib.add(c, "Items")
    lib.add(c, "Ressources")

    # game mechanics
    m = "Mechanics"
    lib.add(m, "Permadeath")
    lib.add(m, "Avoiding Unkillable Objects")
    lib.add(m, "Instant Death")
    lib.add(m, "Game Repeats Until You Die")
    lib.add(m, "Remember an Increasing Number of Things")
    lib.add(m, "Forced Constant Movement")
    lib.add(m, "Game Keeps Gets Harder Until You Die")
    lib.add(m, "Uncountable Number of Possible Paths")
    lib.add(m, "Cut Off One Head, Two Grow Back")
    lib.add(m, "Gravity")
    lib.add(m, "Control multiple characters")
    lib.add(m, "Protect a Target")
    lib.add(m, "Undirected Exploration")
    lib.add(m, "Buy Low, Sell High")
    lib.add(m, "Building")
    lib.add(m, "Brawling")

    # add patterns
    gen.add("A #Genre game where you #Action #Objects")
    gen.add("A #Genre Game about #Objects . But be careful of #Objects !")
    gen.add("A #Genre #Genre Mix with #Objects")
    gen.add("A #Genre Game where you must collect #Collectibles and #Enemies try to stop you.")
    gen.add("A Game about #Objects and #Enemies with ' #Mechanics ' Mechanics.")

    root = tk.Tk()
    root.geometry("600x50")
    root.title("Game Idea Generator")
    idea_text_var = tk.StringVar(root)
    idea_text = tk.Label(root, textvariable=idea_text_var)
    idea_text.pack()
    idea_text_var.set(generate_text(lib, gen))

    button = tk.Button(root, text="Generate Idea", command= lambda: idea_text_var.set(generate_text(lib, gen)))
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()