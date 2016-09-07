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

import maps
import random
import characters
import functions

#This is the main game engine
class Engine(object):

    def game(self):

        map_one = maps.Map()
        player = characters.Player()

        print "Welcome to the game!  Please enter your name:"
        player.name = raw_input("> ")

        room = map_one.rooms['Prologue']
      
        #Each exit from each room returns the next room
        while room != 'Finished':
            next_room = room.enter(player)
            room = map_one.rooms[next_room]

        #Final message, delivered after "Finished" is returned from the loop above.
        print "You have finished the game!  Cool!"


class CombatEngine(object):

#TODO:  Need to add interativity to the fight to make it more interesting, variable phrases &c.  
#       it makes sense to keep a list of attack and damaged phrases with the monster classes to
#       keep it specific to each monster.
    def fight(self, player, monsters):
        """handles a fight between the player and enemies"""

        #TODO:  There is no grammar handling here, so single monsters are refered to as plural,
        #       nor are non-standard plurals handled.

        while(player.hit_points > 0) and (len(monsters) > 0):

            #this is only set to true of the player drinks a potion
            skip_player = False

            print "----------" * 5
            print "You now have", player.hit_points, "hit points."
            print "You face", len(monsters), monsters[0].name, "\bs!"

            #Debugging only
            #for i in range(0,len(monsters)):
            #    print monsters[i].name, "number", i, "has", monsters[i].hit_points, "hit points."
            #End debugging only

            #Combat options for the player are handled first
            print "What would you like to do?"
            print "1) Attack  2) Dodge  3) Drink Heal Potion  4) Run"
            choice = functions.get_choice(4)
            if choice == 1:
                player.dodge_bonus = 0
                player.attack_bonus = 0
            elif choice == 2:
                player.dodge_bonus = 5
                player.attack_bonus = -5
            elif choice == 3:
                player.drink_heal()
                skip_player = True
            else:
                print "You quickly leave the room."
                return "Defeat"

            #set the monster's attack or dodge choice
            for counter in range(0, min(len(monsters), 4)):
                if random.randint(1,2) == 1:
                    monsters[counter].dodge_bonus = 5
                    monsters[counter].attack_bonus = -5
                else:
                    monsters[counter].dodge_bonus = 0
                    monsters[counter].attack_bonus = 0

            #if the player drank a potion they skip their turn.
            if skip_player == True:
                for counter in range(0, min(4, len(monsters))):
                    self.attack(monsters[counter], player)
                continue

            #Now we see who goes first
            if(random.randint(0,1) == 0): 
                print "You won the inititive!"
                self.attack(player, monsters[0]) 
                if monsters[0].hit_points < 1:
                    monsters.pop(0)
                #Now we see if any monsters are left, and if so four of them attack.
                if len(monsters) > 0:
                    for counter in range(0, min(4, len(monsters))):
                        self.attack(monsters[counter], player)
            else:
                #Same as above here, but in reverse order, and the checking is to make sure the player
                #is still alive.
                print "Your enemy won the inititive!"
                for counter in range(0, min(4, len(monsters))):
                    self.attack(monsters[counter], player)
                if(player.hit_points > 0):
                    self.attack(player, monsters[0])
                    if monsters[0].hit_points < 1:
                        monsters.pop(0)
        
        #Once the combat has ended, we see who's left standing.
        if(player.hit_points <= 1):
            print "The monsters have defeated you!"
            print "----------" * 5 
            return "Defeat" 
        else:
            print "You have defeated the enemies!"
            print "----------" * 5
            return "Victory" 
    
    #The attack method handles the actual combat, and sets the revised hit points for the creatures involved.
    def attack(self, attacker, attacked):
        """handles the mechanics of each attack, and adjusts the object's hit points according to hits"""
        if (random.randint(1,10) + attacker.attack_chance + attacker.attack_bonus) > (random.randint(1,10) + attacked.dodge + attacked.dodge_bonus):
            damage = (random.randint(1,3) + attacker.attack_power - attacked.armor)
            #We need to make sure the defender isn't healed if their armor is stronger than the attack
            if damage < 0: damage = 0
            print "The", attacker.name, "has struck, hurting the", attacked.name, damage, "hit points." 
            attacked.hit_points = attacked.hit_points - damage 
            #We need to check if the defender has any hit points left, so we can print out the right message.
            #Note that death is not handled, as it's different depending on whether the attacker is the player
            #or a monster.
            if attacked.hit_points < 1:
                print "The", attacked.name, "has been defeated!"
            else:
                print "The", attacked.name, "now has", attacked.hit_points, "hit points."
        else:
            print "The", attacker.name, "has missed!"
