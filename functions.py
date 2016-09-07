#This file holds reused functions.  Note that the monster packer functions are not here,
#   but in the characters.py file, since it's much simpler to implement them there.

import sys
import characters
import objects

# get_choice gets input from the user and handles all the error checking to make
# sure the caller gets good input

def get_choice(number):
    """Takes in the number of choices available, returns the choice as an int."""
    while True:
        try:
            choice = int(raw_input("> "))
        except KeyboardInterrupt:
            print "\nOkay, bye!"
            sys.exit()
        except:
            print "You must enter an integer between 1 and", number, "\b."
            continue

        if choice > 0 and choice <= number:
            return choice 
        else:
            print "You must enter an integer between 1 and", number, "\b."

# A simple continue function that is used after every major section to preven
# excessive scrolling.
def continue_game():
    print "----------" * 5
    print "Press <ENTER> or <RETURN> to continue."
    try:
        raw_input("> ")
    except KeyboardInterrupt:
        print "\nOkay, bye!"
        sys.exit()
    except:
        print "Ops!  Something went wrong :/"
        sys.exit()

def ogre_packer(number):
    uglies = []
    for i in range(number):
        ugly = characters.Ogre()
        uglies.append(ugly)
    return uglies


def goblin_packer(number):
    uglies = []
    for i in range(number):
        ugly = characters.Goblin()
        uglies.append(ugly)
    return uglies

def giant_rat_packer(number):
    uglies = []
    for i in range(number):
        ugly = characters.GiantRat()
        uglies.append(ugly)
    return uglies

#number is taken in to be consistant with the calls for other
#monsters, however it is ignored as only one boss is possible
def boss_packer(number):
    ugly = characters.Boss()
    uglies = [ugly]
    return uglies

#inventory management
def check_inventory(player):
    items = {}
    #exiting this loop is handled in a return statement in a menu option
    while True:
        print "----------" * 5
        print "Welcome to inventory management!  You have:"
        print player.heal_potions, "heal potions."
        print "\nCurrently equiped weapon:", player.equiped_weapon[0].name, "\b."
        print "\nCurrently equiped armor:"
        for i in range(0, len(player.equiped_armor)):
            print "\t", player.equiped_armor[i].name

        print "\nYour items:"
       
        count = 1
        for thing in player.inventory:
            print count, ":", thing.name
            items[count] = thing;
            #we iterate even after the last  object is counted so
            #that we will have an extra option later
            count += 1

        print "\nWould you like to equip an item?"
        print "Choose item number, or", count, "to continue."
        choice = get_choice(count)

        if choice == count:
            print "\nDone."
            continue_game()
            return

        else:
            #debugging, just print it to screen to see if it works.
            #print items[choice]

            if isinstance(items[choice], objects.Weapon):
                player.equip_weapon(items[choice])
            elif isinstance(items[choice], objects.Armor):
                player.equip_armor(items[choice])
            else:
                print "Error, cannot equip", items[choice]

            print "\nYou now have", items[choice].name, "equiped!"
