#    copyright 2016 by James Brittain
#
#    This file is part of Sugar Plums.
#
#    Sugar Plums is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#
#    Sugar Plums is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Sugar Plums.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/python2

import engines
import characters
import objects
import functions

player = characters.Player()
combat = engines.CombatEngine()

player.heal_potions = 10


input_okay = False
while input_okay == False:
    print "Would you like to equip a weapon?"
    print "1) Rainbow Sparkle Sword, 2) Sparkle Glitter Blaster, 3) Shimmer Dagger  4) No Weapon"
    try:
        choice = int(raw_input("> "))
    except:
        print "You must choose 1, 2, 3 or 4"

    if choice == 1:
        weapon = objects.RainbowSparkleSword()
        input_okay = True
    elif choice == 2:
        weapon = objects.SparkleGlitterBlaster()
        input_okay = True
    elif choice == 3:
        weapon = objects.ShimmerDagger()
        input_okay = True
    elif choice == 4:
        weapon = objects.BareHands()
        input_okay = True
    else:
        print "You must choose 1, 2 or 3"

    player.equip_weapon(weapon)
    player.inventory.append(weapon)

print "Would you like to equip the Magic Shield?"
print "1) Yes, Enter for No"
choice = raw_input("> ")
if choice == '1':
    shield = objects.MagicShield()
    player.equip_armor(shield)
    player.inventory.append(shield)

print "Would you like to equip the Breast Plate?"
print "1) Yes, Enter for No"
choice = raw_input("> ")
if choice == '1':
    plate = objects.BreastPlate()
    player.equip_armor(plate)
    player.inventory.append(plate)

print "Player armor is", player.armor
print "Player dodge is", player.dodge
print "Player attack power is", player.attack_power
print "Player attack chance is", player.attack_chance
print "Now we will look at you inventory."

functions.check_inventory(player)


def get_number():

    print "How many would you like to fight?"
    input_okay = False
    while input_okay == False:
        try:
            choice = int(raw_input("> "))
        except:
            print "You must choose a positive integer between 1 and 10"
        if choice > 0 and choice < 11:
            return choice
        else: 
            print "You must choose a positive integer between 1 and 10"

print "Which type of enemy would you like to fight?"
print "1) Ogre"
print "2) Goblin"
print "3) Giant Rat"
print "4) Boss"
input_okay = False
while input_okay == False:
    try:
        choice = int(raw_input("> "))
    except:
        print "You must choose 1, 2, 3, or 4.  (exception)"
        continue

    if choice < 1 or choice > 4:
        print "You must choose 1, 2, 3, or 4.  (error checking)"
    elif choice == 1:
        number = get_number()
        uglies = functions.ogre_packer(number)
        input_okay = True
    elif choice == 2:
        number = get_number()
        uglies = functions.goblin_packer(number)
        input_okay = True
    elif choice == 3:
        number = get_number()
        uglies = functions.giant_rat_packer(number)
        input_okay = True
    elif choice == 4:
        #number must be 1 for the boss
        uglies = functions.boss_packer(1)
        input_okay = True

combat.fight(player, uglies)
