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

#TODO:  Game balancing!  The fights are not at all balanced

import random
import objects

class Player(object):

    #These values are reassigned in the __init__ method
    hit_points = 0
    max_hit_points = 0
    attack_power = 0
    attack_chance = 0
    armor = 0
    dodge = 0

    #This should be changed at some point for user input
    name = "Player"
    combat_name = "Player"
    combat_name_cap = "Player"

    dodge_bonus = 0
    attack_bonus = 0

    # heal potions are handled seperate from the rest of inventory to simplify
    # certain functions
    heal_potions = 0

    #we start out with nothing.
    inventory = []

    #we need to store currently equiped items
    equiped_weapon = []
    equiped_armor = []

    def __init__(self):
        self.max_hit_points = random.randint(10,20)
        self.hit_points = self.max_hit_points
        bare_hands = objects.BareHands()
        self.inventory.append(bare_hands)
        no_armor = objects.NoArmor()
        self.inventory.append(no_armor)
        self.equip_weapon(bare_hands)
        self.equip_armor(no_armor)
        self.dodge = random.randint(6,11)

    def equip_weapon(self, weapon):
        self.attack_power = weapon.attack_power
        self.attack_chance = weapon.attack_chance
        #For the armor we must remove the currently equiped item.
        if len(self.equiped_weapon) > 0: 
            self.equiped_weapon.pop()
        self.equiped_weapon.append(weapon)

    def equip_armor(self, armor):
        self.armor = self.armor + armor.armor
        self.dodge = self.dodge - armor.dodge_penalty
        #first we must remove "no armor" if it is there.
        for i in range(len(self.equiped_armor)):
            if isinstance(self.equiped_armor[i], objects.NoArmor):
                self.equiped_armor.pop(i)
        #for armor we can just add it to the equiped list, as nothing conflicts.
        self.equiped_armor.append(armor)

    def unequip_armor(self, armor):
        self.armor = self.armor - armor.armor
        self.dodge = self.dodge + armor.dodge_penalty

    def drink_heal(self):
        if self.heal_potions > 0:
            self.hit_points = self.hit_points + 10
            if self.hit_points > self.max_hit_points:
                self.hit_points = self.max_hit_points
            print "You drank a heal potion!  You now have", self.hit_points, "hit points."
        else:
            print "You do not have any heal potions!"

class Monster(object):

    # These values are reassigned in the __init__ method of the child classes
    hit_points = 0
    attack_power = 0
    attack_chance = 0
    armor = 0
    dodge = 0

    # attack and dodge bonuses are calculated per-round in combat and are not set when the 
    # creature is created.
    attack_bonus = 0
    dodge_bonus = 0
    name = "You forgot to name the subclass"
    combat_name = "this needs to be changed by the subclass"
    combat_name_cap = "You forgot this too"

class Ogre(Monster):

    name = "Ogre"
    combat_name = "the ogre"
    combat_name_cap = "The ogre"


    def __init__(self):
        self.hit_points = random.randint(5,10)
        self.attack_power = random.randint(5,9)
        self.armor = random.randint(4,7)
        self.attack_chance = random.randint(3,6)
        self.dodge = random.randint(2,6)

class Goblin(Monster):

    name = "Goblin"
    combat_name = "the goblin"
    combat_name_cap = "The goblin"

    def __init__(self):
        self.hit_points = random.randint(5,7)
        self.attack_power = random.randint(4,6)
        self.armor = random.randint(3,5)
        self.attack_chance = random.randint(3,5)
        self.dodge = random.randint(2,4)

class GiantRat(Monster):

    name = "Giant Rat"
    combat_name = "the giant rat"
    combat_name_cap = "The giant rat"

    def __init__(self):
        self.hit_points = random.randint(1,3)
        self.attack_power = random.randint(1,3)
        self.armor = random.randint(1,2)
        self.attack_chance = random.randint(2,4)
        self.dodge = random.randint(1,2)

class Boss(Monster):

    #Change this
    name = "Boss"
    combat_name = "the boss"
    combat_name_cap = "The boss"

    def __init__(self):
        self.hit_points = random.randint(20,30)
        self.attack_power = random.randint (15,25)
        self.armor = random.randint(10,15)
        self.attack_chance = random.randint(10,15)
        self.dodge = random.randint(10,15)


        
