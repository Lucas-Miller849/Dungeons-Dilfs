from tkinter import *
from dungeon_generator import *
from sys import *
from monster_generator import *

#master = Tk()

top = Tk()
top.title("Dungeons & Dilfs")

L1 = Label(top, text='Dugeon Generator')
L1.pack(side = TOP)

def gen_dungeon():
    generate_dungeon()

b = Button(top, text="Start", command=gen_dungeon,height=50,width=50)
b.pack()
b.config(relief=RAISED)

frame = Frame(width=1000, height=500, bd=1, relief=RAISED)
frame.pack(fill=X, padx=5, pady=5)
frame.pack_propagate(0)


def populate_dungeon():
    pass

def generate_dungeon():
    gen = Generator()
    gen.gen_level()
    gen.gen_tiles_level()
    populate_dungeon()
    menu()

def generate_monster():
    monster_menu()
    menu()

def something():
    pass 

def menu():
    print (30 * '-')
    print ("   M A I N - M E N U")
    print (30 * '-')
    print ("1. Generate Dungeon")
    print ("2. Generate Monster")
    print ("3. Exit")
    print (30 * '-')
 
## Get input ###
    choice = input("Enter your choice [1-3] : ")
 
### Convert string to int type ##
    choice = int(choice)
 
### Take action as per selected menu-option ###
    if choice == 1:
            print ("Generating Dungeon...")
            generate_dungeon()
            populate_dungeon()
    elif choice == 2:
            print ("Generating Monster...")
            generate_monster()
    elif choice == 3:
            print ("Exiting...")
            exit()
    else:
            print ("Invalid number. Try again...")

menu()



#top.mainloop()
