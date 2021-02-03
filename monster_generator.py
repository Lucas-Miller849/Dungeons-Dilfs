import random 
from PIL import Image
import sys

cockatrice = Image.open("/Users/lucasmiller/Downloads/hho_cockatrice.jpg")
blight = Image.open("/Users/lucasmiller/Downloads/hho_blight.jpg")
bullywug = Image.open("/Users/lucasmiller/Downloads/hho_bullywug.jpg")
wolf = Image.open("/Users/lucasmiller/Downloads/Gwent_cardart_monsters_wolf.jpg")
goblin = Image.open("/Users/lucasmiller/Downloads/Goblin.png")
quasit = Image.open("/Users/lucasmiller/Downloads/hho_quasit.jpg")

hp = 0
ac = 0

level_one = ["Wolf", "Blight","Goblin","BullyWug"]
level_one_hp = ["7","5","9"]
level_one_ac = ["13","15","14"]
monster_one = ""
monster_one_hp = ""
monster_one_ac = ""

level_two = ["Wolf","Blight","Quasit"]
level_two_hp = ["8","10","11"]
level_two_ac = ["13","14","15"]
monster_two = ""
monster_two_hp = ""
monster_two_ac = ""

level_three = []
level_three_hp = []
level_three_ac = []
monster_three = ""
monster_three_hp = ""
monster_three_ac = ""

level_four = []
level_four_hp = []
level_four_ac = []
monster_four = ""
monster_four_hp = ""
monster_five_ac = ""



def generate_stats(cr = 0):
    if cr < 1:
        if random.choice(level_one) == "Goblin":
            goblin.show()
            print("Goblin")
        elif random.choice(level_one) == "Blight":
            blight.show()
            print("Blight")
        elif random.choice(level_one) == "BullyWug":
            bullywug.show()
            print("BullyWug")
        elif random.choice(level_one) == "Wolf":
            wolf.show()
            print("Wolf")
        else:
            print("shit")
        print("HP = " + random.choice(level_one_hp))
        print("AC = " + random.choice(level_one_ac))
    elif  1 < cr < 2:
        if random.choice(level_two) == "Goblin":
            goblin.show()
            print("Goblin")
        elif random.choice(level_two) == "Blight":
            blight.show()
            print("Blight")
        elif random.choice(level_two) == "BullyWug":
            bullywug.show()
            print("BullyWug")
        elif random.choice(level_two) == "Wolf":
            wolf.show()
            print("Wolf")
        elif random.choice(level_two) == "Quasit":
            quasit.show()
            print("Quasit")
        else:
            print("shit")
        print("HP = " + random.choice(level_two_hp))
        print("AC = " + random.choice(level_two_ac))
    elif cr < 3:
        if random.choice(level_three) == "Goblin":
            goblin.show()
            print("Goblin")
        elif random.choice(level_three) == "Blight":
            blight.show()
            print("Blight")
        elif random.choice(level_three) == "BullyWug":
            bullywug.show()
            print("BullyWug")
        elif random.choice(level_three) == "Wolf":
            wolf.show()
            print("Wolf")
        elif random.choice(level_three) == "Quasit":
            quasit.show()
            print("Quasit")
    elif cr < 4:
        print("Level 4 Monster")
 #       if random.choice(level_four) == "Goblin":
 #           pass

def monster_menu():
    print (30 * '-')
    print ("   Generate Monster")
    print (30 * '-')
    print ("1. Level 1")
    print ("2. Level 2")
    print ("3. Level 3")
    print ("4. Level 4")
    print ("5. Exit")
    print (30 * '-')
 
## Get input ###
    choice = input('Enter your choice [1-3] : ')
 
### Convert string to int type ##
    choice = int(choice)
 
### Take action as per selected menu-option ###
    if choice == 1:
            print ("Generating Level 1 Monster...")
            generate_stats(.25)
    elif choice == 2:
            print ("Generating Level 2 Monster...")
            generate_stats(1.25)
    elif choice == 3:
            print ("Generating Level 3 Monster...")
            generate_stats(2.25)
    elif choice == 4:
            print("Generating Level 4 Monster...")
            generate_stats(3.25)
    elif choice == 5:
            print("Exiting...")
            exit()
    else:
            print ("Invalid number. Try again...")

monster_menu()