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

import random
import engines
import characters
import objects
import functions

#Main class all the rooms will inheret from.  Will contain random encounters
class Room(object):
    pass

class Prologue(Room):

    def enter(self, player):
         print "----------" * 5
         print "Welcome to the game!  You,", player.name, "\b, are a Sugar Plum Fairy." 
         print "You live under Bumbly Hill where you use magic fairy dust"
         print "to make the most scrumptious carmel chocolate swirl bundt cake"
         print "ever eaten by fairy, monster or human in all the magic kingdoms."
         print "The annual Fairy City bake off is in just three days, but you"
         print "have run out of fairy dust!  The only source in all of Fairy"
         print "Land is the Dark Dungeon of Deepest Dispair.  You must be brave"
         print "and resourseful if you are to compete in the annual bake off!"
         functions.continue_game()
         return "Enterence"
    
class Enterence(Room):

    dead_rats = False
    
    def enter(self, player):
        print "---------" * 5
        print "You descend into the gloomy enterence hall of the dungeon."
        print "On the walls you see pictures of horrific monsters and"
        print "and terrible beasts."
        if self.dead_rats == False:
            print "\nTwo giant rats scurry from the shadows!"
            print "You get ready for a fight!"

            rats = functions.giant_rat_packer(2)
            combat = engines.CombatEngine()
            result = combat.fight(player, rats)

            if result == "Victory":
                self.dead_rats = True
                print "Having bested your first opponents, you venture further into the dungeon."
                functions.continue_game()
                return 'MainHall'
            else:
                print "You retreat out of the dungeon!  Too bad about that, there's no way you"
                print "can get your Fairy City Bake Off trophy now!"
                functions.continue_game()
                return 'Defeat'

        #Main loop for the room.  Only 'check inventory' doesn't exit the room.
        sanity_check = 1
        while sanity_check < 100: 
            sanity_check 
            print "There are two dead rats on the floor here.  Do you wish to"
            print "leave the dungeon, or venture further in?"
            print "\n1) Go further into the dungeon  2) Leave  3) Check Inventory"
            choice = functions.get_choice(3)

            if choice == 2:
                print "Are you sure?  The game will end if you leave!"
                print "1) to turn around and go into the main hall  2) leave"
                choice2 = functions.get_choice(2) 
                if choice2 == 1:
                    print "You retreat out of the dungeon!  Too bad about that, there's no way you"
                    print "can get your Fairy City Bake Off trophy now!"
                    functions.continue_game()
                    return 'Defeat'
                else:
                    print "You venture further into the dungeon."
                    functions.continue_game()
                    return 'MainHall'

            elif choice == 3:
                functions.check_inventory(player)

            else:
                print "You venture further into the dungeon."
                functions.continue_game()
                return 'MainHall'
        print "Ops, something went wrong."
        return 'Error'

class MainHall(Room):

    # Set the state of the room at the start.  Encounters in the room will change these so events don't
    # trigger multiple times.
    heal_potions = True
    got_dagger = False
    goblins = True
    talking_door = True
    
    def enter(self, player):
        sanity_check = 1
        while sanity_check < 100:
            print "----------" * 5
            print "The great hall is huge, stretching out into darkness above you."
            print "There's an eeire feeling here, like something is watching you."
            print "There are dark shadows on the left side of the room, and a pile"
            print "of rubble on the right.  Doors open to the north, east, and south."
            print "The east door leeds to the enterence room you began in."
            print "\nWhat would you like to do?"
            print "1) Investigate the dark shadows"
            print "2) Investigate the pile of rubble"
            print "3) Go through the door to the north"
            print "4) Go through the door to the east, to the enterence hall"
            print "5) Go through the door to the south"
            print "6) Inventory Management"

            choice = functions.get_choice(6)

            print "----------" * 5

            #dark shadows
            if choice == 1:
                print "With great trepidation you creep into the darkness.  Something"
                print "scurries past your leg!  You jump back, but it's too late!"
                print "Giant rats scurry out of the darkness and attack you!"

                rats = functions.giant_rat_packer(random.randint(2,5))
                fight = engines.CombatEngine()
                result = fight.fight(player, rats)

                if result == 'Victory':
                    print "You manage to defeat the giant rats!  Poking around the darkness"
                    print "you discover huge holes the rats have dug into the ground."

                    if self.heal_potions == True:
                        print "You find two heal potions in the dirt around the holes!"
                        player.heal_potions = player.heal_potions + 2
                        self.heal_potions = False
                    
                    print "Fearing more rats could come up and attack at any moment,"
                    print "you quickly leave the darkness and return to the middle of the room."
                    functions.continue_game()

                if result == 'Defeat':
                    print "Pressed back by the vicious rats, you are forced to retreat to"
                    print "the enterence hall!"
                    functions.continue_game()
                    player.hit_points = 10
                    return 'Enterence'
           
            #rubble pile
            elif choice == 2:
                print "Chuncks of rock from the wall are piled here, along with odd"
                print "pieces of wood and broken chairs."

                if self.got_dagger == False:
                    print "\nDigging through the rubble you find a gold hilted shimmer dagger!"  
                    print "It fits your tiny fairy hand perfectly."

                    dagger = objects.ShimmerDagger()
                    player.inventory.append(dagger)
                    self.got_dagger = True

                    print "\nWould you like to equip the dagger?"
                    print "1) yes  2) no"
                    choice = functions.get_choice(2)

                    if choice == 1:
                        player.equip_weapon(dagger)
                        print "\nThe weapon feels good in your hand!"
                    else:
                        print "\nYou slip the dagger into your pack in case you need it later."

                    print "\nWhen you are convinced there is nothing else of worth in the pile,"
                    print "you return to the center of the room."
                    functions.continue_game()

                else: 
                    print "\nYou find nothing of value here.  When you are finished"
                    print "searching, you return to the center of the room."
                    functions.continue_game()

            # northern door
            elif choice == 3:
                if self.talking_door:
                    print "The northern door shows interlocking symbols that weave into"
                    print "and out of each other. You cannot open the door, but as you try"
                    print "two round, yellow eyes open in the wood, and a long, thin mouth"
                    print "opens besides the door knob."
                    print "\n\"Welcome, brave fairy!  To open this door you must first answer my riddle."
                    print "What is round and blue and white, and spins but never rolls?\""
                    print "----------" * 5
                    print "How do you answer?"
                    print "1)  A marble"
                    print "2)  The earth"
                    print "3)  A dolphin"
                    print "4)  A cloud"
                    choice = functions.get_choice(4)

                    if choice == 2:
                        print "The door smiles broadly, then breaks into a shrill, cackling laugh."
                        print "\"Yes, yes!\" it cries out, and the door swings open.  You step through."
                        self.talking_door = False
                        functions.continue_game()
                        return 'PuzzleOne'
                    else:
                        print "\"Bah!\" cries the door.  \"I thought you would be the one.\"  It looks"
                        print "disapointed as it vanishes back into the wood.  You walk back to the center"
                        print "of the room."
                        functions.continue_game()

                else:
                    print "The door here hangs open and shows no signs of its previous animation."
                    print "Would you like to step through the open door?"
                    print "1) Yes  2) No"
                    choice = functions.get_choice(2)

                    if choice == 1:
                        print "You step through the open door."
                        return 'PuzzleOne'
                    else:
                        print "Thinking better of it, you step away from the door"
                        print "and return to the center of the room."


            # return to enterence room
            elif choice == 4:
                print "Unsure of yourself, you retreat fearfully into the enterence"
                print "hall, wondering if you are really strong enough to compete in" 
                print "the annual Fairy City bake off."
                functions.continue_game()
                return 'Enterence'

            # southern door
            elif choice == 5:
                if self.goblins:
                    print "You walk boldly across the room toward the southern door."
                    print "Pictures on the wall show all sorts of scary monsters.  There"
                    print "are goblins, ogres, trolls, and some huge, scaley beast that"
                    print "lurks behind the rest, hidden from view."
                    print "\nYou realize two goblins are guarding the door!  As you approach,"
                    print "one of them says, \"Look Fizzgot, the little fairy!  You like to" 
                    print "smash little fairy?\"  The other one smiles, and you recoil from"
                    print "its reeking breath and broken teeth."
                    print "----------" * 5
                    print "What do you do?"
                    print "1) Charge in and attack!"
                    print "2) Retreat to the center of the room."
                    choice = functions.get_choice(2)

                    if choice == 1:
                        print "Yelling your squekie battle cry, you charge at the monsters!"
                        fight = engines.CombatEngine()
                        goblins = functions.goblin_packer(2)
                        result = fight.fight(player, goblins)

                        if result == 'Victory':
                            print "Beaten, the goblins run shrieking from the room, leaving the door"
                            print "open behind them. You don't think you'll be seeing those two again."
                            print "You boldly stride through the door."
                            self.goblins = False
                            functions.continue_game()
                            return 'MonsterOne'
                        else:
                            print "You retreat from the fury of the goblin's attack, running all"
                            print "the way back into the enterence hall to hide and regroup."
                            #We heal the player a bit.  This is a kids game....
                            player.hit_points = 10
                            functions.continue_game()
                            return 'Enterence'

                    else:
                        print "You back away from the two, slipping into the shadows."
                        print "\"Hey, where she go?\" asks the uglier one."
                        print "\"Forget it Snog, we guard door, not chase fairy, or boss get mad.\"  Relieved, you retreat to the"
                        print "center of the room."
                        functions.continue_game()

                else:
                    print "You see signs of a fight as you approach the door, but there are no signs"
                    print "of monsters.  The door is open, would you like to step through?"
                    choice = functions.get_choice(2)

                    if choice == 1:
                        print "You step through the door."
                        return 'MonsterOne'

                    else:
                        print "You step away from the door and return to the center of the room."

            elif choice == 6:
                functions.check_inventory(player)

            else:
                print "Woops!  An error has occured."
                return 'Error'

class MonsterOne(Room):

    goblins_defeated = False
    got_magic_shield = False

    def enter(self, player):

        sanity_check = 1
        while sanity_check < 100:

            if self.goblins_defeated == False:
                print "You barge into the room, only to realize that a part of goblins"
                print "stand ready, rusty swords to hand!  You suddenly find youself"
                print "in combat!"

                uglies = functions.goblin_packer(random.randint(4,6))
                fight = engines.CombatEngine()
                result = fight.fight(player, uglies)

                if result == "Victory":
                    print "As you pummel the last of the goblins, they run shrieking from the room,"
                    print "dragging their injured companions as they go.  In their hurry to retreat,"
                    print "They've dropped two heal potions!  You quickly pick them up."
                    functions.continue_game()
                    player.heal_potions += 2
                    self.goblins_defeated = True

                elif result == "Defeat":
                    print "Recoiling from the ferocity of the goblin's attack, you are forced back"
                    print "through the door into the main hall."
                    functions.continue_game()
                    player.hit_points = 10
                    return "MainHall"

                #This should never come up, but just in case....
                else: 
                    print "Something went wrong!"
                    return "Error"

            else:
                print "There are signs of a big fight here, but no sign of any monsters."

            # Main room description after the goblins have been delt with.
            print "\nThis room is filthy, with rusty weapons, discarded, rotting meat, and other refuse"
            print "strewn about.  The stone walls are bare, with big splotchy stains and deep gouges."
            print "There is a door to the north which leads to the main hall, another door to the west"
            print "which has been locked from the other side, and a huge pile of rubble."
            print "\nWhat would you like to do?"
            print "1) Search through the pile of rubble."
            print "2) Go through the door to the north, back to the main hall."
            print "3) Investigate the locked door to the west."
            print "4) Inventory Management."
            choice = functions.get_choice(4)

            if choice == 1:
                print "----------" * 5
                print "The rubble pile is truely digusting, full of half eaten sandwhiches and goblin"
                print "toe nail clippings.  Holding your breath so you don't have to smell it, you"
                print "shift through the filth.\n"
                
                if self.got_magic_shield == False: 
                    
                    print "Your search turns up a small sheild. It's perfectly sized for"
                    print "your little fairy body, and you pick it up and clean it on some discarded"
                    print "cloth.  It's so light and strong, it must be magical!"
                    shield = objects.MagicShield()
                    player.inventory.append(shield)
                    self.got_magic_shield = True

                    print "Would you like to equip the shield?"
                    print "1) Yes  2) No"
                    choice2 = functions.get_choice(2)
                    if choice2 == 1:
                        player.equip_armor(shield)
                        print "The shield feels light and comfortable in your hands."
                    else:
                        print "You slip the shield into your pack and continue on your way."

                    functions.continue_game()

                else:
                    print "Despite your search, you find nothing of value."
                    functions.continue_game()
                    

            elif choice == 2:
                print "----------" * 5
                print "Stepping carefully so you don't trip on anything, you make your way to the door"
                print "and step into the main hall."
                functions.continue_game()
                return "MainHall"

      

            elif choice == 3:
                sanity_check = 1
                while sanity_check < 100:
                    sanity_check += 1 
                    print "----------" * 5
                    print "The doors is locked up tight.  The goblins must have slammed it behind them"
                    print "in their flight.  The door itself is quite sterdy, but the leather hinges are"
                    print "on your side of the door."
                    print "\nWhat would you like to do?"
                    print "1) Pick the lock."
                    print "2) Cut the leather hinges."
                    print "3) Try to bash the door down."
                    print "4) Return to the center of the room."
                    choice = functions.get_choice(4)

                    if choice == 1:
                        #set a small chance the attempt is sucessful.
                        print "You spend about ten minutes fiddling with the lock.  Too bad you don't have"
                        print "better tools!"
                        if random.randint(1,20) == 1:
                            print "\nWhen you are just about to give up, the lock clicks and the door swings open!"
                            print "Steeling yourself against what must be behind the door, you step through."
                            functions.continue_game()
                            return "MonsterTwo"
                        else:
                            print "\nDespite your best efforts, you are unable to get the lock to open."
                            functions.continue_game()

                    elif choice == 2:
                        print "----------" * 5
                        print "The leather hinges are badly worn and cracked.  You don't think it will be that difficult."

                        #We need to check the player's inventory to see if they have a weapon.
                        for i in range(0, len(player.inventory)):
                            if isinstance(player.inventory[i], objects.Weapon) and player.inventory[i].name != "Bare Hands":
                                print "With your", player.inventory[i].name, "you easily cut away the leather and pry"
                                print "the door open.  Taking a deep breath, you step through the door,"
                                print "afraid and exilerated by what might be there."
                                functions.continue_game()
                                return "MonsterTwo"

                        #If the above loop finishes without reaching its condition we have failed with the door:
                        print "Despite your best efforts you cannot pry the leather apart with your"
                        print "bare hands.  If only you could find a weapon of some kind!"

                    elif choice == 3:
                        print "You crash into the heavy door with your little fairy body.  It doesn't budge."
                        functions.continue_game()

                    #break out of the nested loop into the main room's loop 
                    else: 
                        break

            #if the player chooses inventory management
            else:
                functions.check_inventory(player)

class MonsterTwo(Room):

    sanity_check = 1
    ogres = True
    glitter_blaster = True
   
    def enter(self, player):
        while self.sanity_check < 100:

            if self.ogres == True:
                print "Stepping through the door you almost walk into the great, hairy body of an ogre."
                print "As he slowly turns around you realize that it's a whole family, gorging themselves"
                print "on a bucket of snail pudding.  \"What it be?\" one asks.  \"Me don't know, but"
                print "me smash!\" yells another as they all raise heavy clubs."

                uglies = functions.ogre_packer(random.randint(5,8))
                fight = engines.CombatEngine()
                result = fight.fight(player, uglies)

                if result == 'Victory':
                    print "The defeated ogres flee the room, crying and hollering in terror.  They've"
                    print "left behind two heal potions!  You quickly pick them up."
                    self.ogres = False
                    player.heal_potions += 2

                else:
                    print "The ogre's assult is too ferocious to you!  You flee before they can kill you."
                    print "Maybe you need to find better weapons before you try again?"
                    player.hit_points = 10
                    return 'MonsterOne'

            else:
                print "There are signs of a battle here, and a half-eaten pot of reeking ogre-stew, but"
                print "no signs of monsters."

            #main room description
            print "Besides the pot of ogre stew, the room is pretty barren.  There's sack left"
            print "by the ogres, some smouldering wood, and a door on the far side of the room."
            print "\nWhat would you like to do?"
            print "1) Look through the sack."
            print "2) Investigate the smouldering logs."
            print "3) Check the door to the west."
            print "4) Go through the door to the east, back to the goblin's room."
            print "5) Inventory management."

            choice = functions.get_choice(5)

            if choice == 1:
                if self.glitter_blaster == True:
                    print "Looking through the sack, you find a rusty pair of hedge trimmers, a large"
                    print "jar holding an ogre's belly button lint collection."
                    print "You also find a small magical wand.  You quickly pick up the wand, recognizing"
                    print "it as the fabled Glitter Blaster of Septemius the Happy Baker!"
                    glitter_blaster = objects.SparkleGlitterBlaster()
                    player.inventory.append(glitter_blaster)
                    self.glitter_blaster = False

                    print "\nWould you like to equip the weapon?"
                    print "1) Yes,  2) No"
                    choice2 = functions.get_choice(2)
                    if choice2 == 1:
                        player.equip_weapon(glitter_blaster)
                        print "The wand feels natural in your hand, like a missing finger come home."
                        functions.continue_game()

                    else:
                        print "Confident in your abilities, you slip the weapon into your sack."

                else:
                    print "You look through the sack, but find nothing but rusty hedge trimmers, and"
                    print "a large jar holding an ogre's belly button lint."
                    functions.continue_game()

            elif choice == 2:
                print "On closer examination, you realize the ogre's were burning cow patties!"
                print "You scorch your hand on an ember as you poke around it, losing 2 hit points."
                player.hit_points -= 2
                if player.hit_points < 1:
                    print "Fingers burning, you have to flee back into the goblin's room to find some water"
                    print "to quench them."
                    player.hit_points = 10
                    return 'MonsterOne'

            elif choice == 3:
                print "The door has a large sign on it which ready: \"Da Boss\". The door isn't locked,"
                print "but you feel great trepidation.  Is this really a good idea?  Behind this door"
                print "is the only source of fairy dust in all of Fairy Land, and you just need"
                print "it to do well in the bake off!  But are you truely ready?"
                print "\nDo you venture through the door?"
                print "1) Yes,  2) No"
                choice = functions.get_choice(2)

                if choice == 1:
                    print "You take a deep breath and steady yourself.  This is your last chance"
                    print "to check your inventory before the big confrontation, would you like to?"
                    print "1) check inventory, 2) continue"
                    if functions.get_choice(2) == 1:
                        functions.check_inventory(player)
                    print "When you are ready you step through the final door"
                    print "of the dungeon."
                    functions.continue_game()
                    return "Boss"

                else: 
                    print "'No, I'm not quite ready yet' you think to yourself, and step away from the door."

            elif choice == 4:
                print "Unsure if you're ready to press on, you backtrack to the goblin's room."
                return 'MonsterOne'

            else:
                functions.check_inventory(player)

        print "Ops!  Something went wront."
        return 'Error'


class PuzzleOne(Room):

    #room contents, set to true until they player gets them.
    magic_sword = True
    plate_armor = True
    heal_potions = 5

    riddle_one_solved = False
    riddle_two_solved = False
    riddle_three_solved = False
    riddle_four_solved = False
    riddle_five_solved = False
    
    all_solved = False

    #The riddle order is meant to be random and confusing.  The fairy moves on
    #from wrong answers and cycles through them at random until they are all solved.
    #each riddle should include an escape mechanism
    def riddle_one(self,player):
        print "Oh I know, I'll ask the one about the tiger."
        print "What has a head, a tail, is brown, but has no legs?"
        print "\nWhat do you say?"
        print "1)  \"Uh, hello, my name is", player.name, "\b."
        print "2)  \"A penny.\""
        print "3)  \"A tiger?\""
        print "4)  \"A brown snake."
        print "5)  \"Never mind this, I'm leaving the room.\""
        choice = functions.get_choice(5)
        
        if choice == 1:
            print "\"What does that have to do with anything, silly?  My name is Igglesbottom"
            print "for all the difference it makes!  Silly fairy!"
            return
        elif choice == 2:
            print "\"What?  You got it right?  How did you guess that?  I'm amazed.\"  She is"
            print "obviously delighted.  \"Let me see here, for that one you win, let me see,\""
            print "She pulls out a small scrap of paper from a puch at her side."
            print "lets see, yes, you win this magical breast plate!\"  She pulls from the"
            print "timy pouch a full breast plate that looks custom made for your fairy body."
            breast_plate = objects.BreastPlate()
            player.inventory.append(breast_plate)
            print "\nWould you like to equip it?"
            print "1) Yes,  2) No"
            choice = functions.get_choice(2)
            if choice == 1:
                player.equip_armor(breast_plate)
                print "You slip into the magical armor.  It fits you perfectly!"
            else:
                print "You slip the armor into your pack, just in case you need it later."
            functions.continue_game()
            return 'Solved'
        elif choice == 3:
            print "What, a tiger?  Wow you sure are silly!  A tiger has legs.  Well, I guess not"
            print "all tigers have legs, but as far as we're concerned.  Although maybe it could"
            print "be a drawing of a tiger with no legs.  But no, you didn't say a drawing.  Anyway"
            print "that's not the correct answer."
            functions.continue_game()
            return
        elif choice == 4:
            print "A brown snake?!  No, of course it isn't a brown snake, a brown snake doesn't have a head."
            print "Silly you!  Who ever heard of a brown snake with no legs either.  Oh my goodness.  Okay,"
            print "they do have tails, I grant you that.  Nope, you're gonna have to try again!"
            functions.continue_game()
            return
        else:
            print "Oh, you're no fun anymore!  And I thought you were going to be fun."
            functions.continue_game()
            return 'Escape'

    def riddle_two(self,player):
        print "\"Okay okay, this is a good one.  I'm gonna tell you the moon one, ready?"
        print "What has a hand but isn't alive?\""
        print "\nWhat do you say?"
        print "1) A parsnip"
        print "2) Applause"
        print "3) A leopard skin rug"
        print "4) A mitten"
        print "5) Never mind this, I'm getting out of here."

        choice = functions.get_choice(5)

        if choice == 1:
            print "\"A what?  A parsnip?  Are you crazy, parsnips don't have hands. No no no, or non"
            print "as the french would say.  You're going to have to try again.\""
            functions.continue_game()
            return
        elif choice == 2:
            print "\"Applause?  I get it, give you a hand, ha, that's pretty good!  But no, that's not the"
            print "answer.  See, it says right here, section 3, page 253, paragraph 2:  No player shall"
            print "answer close to the right answer, the answer must be the exact answer as specified by"
            print "the party of the first part, the party of the second part, or the party of the third"
            print "part, if two thirds of parties four, five, six, and seven agree.  So no, you'll have"
            print "to try again, I'm sorry!"
            functions.continue_game()
            return
        elif choice == 3:
            print "Okay, now you're not even trying.  No no no, that is incorrect!"
            functions.continue_game()
            return
        elif choice == 4:
            print "Lets see, hmm, a mitten.  Yep!  Says it right here, a mitten!  Great job!  And as your"
            print "reward I shall grant to thee, I just love using that high falutin' language you know,"
            print "I shall grant to thee two potions of healing!  Yay!"
            player.heal_potions += 2
            self.heal_potions -= 2
            functions.continue_game()
            return 'Solved'
        else:
            print "You're leaving?  Oh and I thought we were having so much fun!"
            functions.continue_game()
            return 'Escape'

    def riddle_three(self,player):
        print "\"Okay okay, this s a good one.  What do you get when you cross a cantalope and an eel?"
        print "OKay, okay, that's not really a riddle, I don't know what that would be!  Okay, here we"
        print "go:  Everyone has one, but nobody can use ever use it.  What is it?  Huh?\""
        print "\nWhat do you say?"
        print "1) A name"
        print "2) an eel?"
        print "3) A antelope?"
        print "4) A shadow"
        print "5) Nevermind, I don't want to play anymore."
        choice = functions.get_choice(5)
        
        if choice == 1:
            print "\"An name?  Well, my name is Igglesbottom, and I use it all the time!  No"
            print "that's silly, you're silly!  Lets try another one.\""
            functions.continue_game()
            return
        elif choice == 2:
            print "\"No no, you're confused about this one.  I knew I shouldn't have made the joke about"
            print "the eel.  Now you're all mixed up.  Look, lets just try another one.\""
            functions.continue_game()
            return
        elif choice == 3:
            print "\"What?  That doesn't make any sense!  Oh, I think you're thinking of the cantalope and"
            print "the eel.  Look, that wasn't a real riddle, okay, you need to listen to the question.\""
            functions.continue_game()
            return
        elif choice == 4:
            print "\"A shadow!  That's right!  You got it right!  Oh this is so exciting.  Okay,"
            print "for getting that one right you get. . . a magic sword!  Its the fabled magic"
            print "Rainbow Sparkle Sword of the fairy Gimbly Two Tones.  Here ya go!\""
            sword = objects.RainbowSparkleSword()
            player.inventory.append(sword)
            print "\nWould you like to equip the sword?"
            print "1) Yes,  2) No"
            choice = functions.get_choice(2)
            if choice == 1:
                print "The sword is light and comfortable in your hand."
                player.equip_weapon(sword)
                functions.continue_game()
            else:
                print "You slip the magic sword into your pack in case you need it later."
                functions.continue_game()
            return 'Solved'
        else:
            print "\"Oh but we were just getting started!  Oh man, and I thought you were going to be fun.\""
            functions.continue_game()
            return 'Escape'

    def riddle_four(self, player):
        print "\"Here we go, this is a tough one:  What tastes better than it smells?\""
        print "\nWhat do you say?"
        print "1)  Hasenpfeffer"
        print "2)  Bubblegum"
        print "3)  Your tongue"
        print "4)  Friendship"
        print "5)  I don't want to play anymore, goodbye!"

        choice = functions.get_choice(5)

        if choice == 1:
            print "No no, that's rabbit stew.  Smells fine!  I see you're going to need some practice,"
            print "so lets try another one."
            functions.continue_game()
            return
        elif choice == 2:
            print "Oh I love the way bubblegum smells!  Yum!  Makes me want to chew a piece right now."
            print "Lets just move along then, okay?"
            functions.continue_game()
            return
        elif choice == 3:
            print "Lets see, hmm, yep!  Says it right here, tongue.  Well, okay!  You won some more"
            print "heal potions!  Yay!"
            player.heal_potions += 3
            functions.continue_game()
            return 'Solved'
        elif choice == 4:
            print "No no no, friendhip doesn't taste or smell!  Are you sure you know what you're talking"
            print "about?  Lets just move on, okay?"
            functions.continue_game()
            return
        else:
            print "But we were just starting to have fun!  Where are you going?"
            functions.continue_game()
            return 'Escape'

    def riddle_picker(self, player):
        sanity_check = 1
        while sanity_check < 100:
            choice = random.randint(1,4)

            if choice == 1 and self.riddle_one_solved == False: 
                result = self.riddle_one(player)
                if result == 'Escape':
                    return 'Escape'
                elif result == 'Solved':
                    self.riddle_one_solved = True

            elif choice == 2 and self.riddle_two_solved == False: 
                result = self.riddle_two(player)
                if result == 'Escape':
                    return 'Escape'
                elif result == 'Solved':
                    self.riddle_two_solved = True
        
            elif choice == 3 and self.riddle_three_solved == False: 
                result = self.riddle_three(player)
                if result == 'Escape':
                    return 'Escape'
                elif result == 'Solved':
                    self.riddle_three_solved = True

            elif choice == 4 and self.riddle_four_solved == False: 
                result = self.riddle_four(player)
                if result == 'Escape':
                    return 'Escape'
                elif result == 'Solved':
                    self.riddle_four_solved = True

#            elif choice == 5 and self.riddle_five_solved == False: 
#                result = self.riddle_five(player)
#                if result == 'Escape':
#                    return 'Escape'
#                elif result == 'Solved':
#                    self.riddle_four_solved = True
            #or else all are solved.
            if self.riddle_one_solved == True and self.riddle_two_solved == True and self.riddle_three_solved == True and self.riddle_four_solved == True:
                #debugging only
                self.all_solved = True 
                return "Finished"
    
    def enter(self, player):
        print "The walls of this room are covered in drawings of lillies and butterflies,"
        print "drawn colorfully by an amature.  In the center a little pixie hovers, paint"
        print "brush in hand."

        if self.all_solved == False:
            print "\"Oh hi!\" she squeaks at you as you come in.  \"I'm so happy that you're here!\""
            print "You smile back, unsure of what this is all about.  \"Okay, so we have to play"
            print "the game.  It's in the rules, look see,\" she says as she pulls out a small"
            print "book.  \"Section 3, paragraph 4, the player must answer the riddles to get"
            print "magic items to help her on her quest.\"  Well that's pretty clear right?  Where"
            print "would you like to start?  Oh I know the perfect one!"
            done = ""
            while done != "Finished":
                done = self.riddle_picker(player)
                if done == 'Escape':
                    print "Before the fairy can get another word out, you quickly leave the room."
                    functions.continue_game()
                    return 'MainHall'

            print "Well, that's all my riddles honey!  Good job!  Time to be about your quest now."
            print "The little fairy picks up her brush and starts coloring in a pansie on her mural."
            functions.continue_game()
            return 'MainHall'

        else:
            print "The fairy Igglesbottom hums a little song to herself as she paints a picture"
            print "on the wall of a duck riding on a platapus' back.  She says nothing,"
            print "too distracted by her work to even notice you.  After a moment, you turn"
            print "and leave her to her work."
            functions.continue_game()
            return 'MainHall'

class Boss(Room):

    def enter(self, player):

        boss = functions.boss_packer(1) 

        print "The room is huge and dark, lit up by the red glow of fire burning somewhere beneath the floor."
        print "At first you see nothing but shadows, and you worry that the fairy dust may not actually"
        print "be here!  Then the room rumbles around you, and you catch a glimpse of a massive, reptillian"
        print "leg moving in the corner of your eye.  When you look closer you see nothing."

        print "\n\"And what is this little one?  A little one has come?\" It's voice is deep and you"
        print "almost bolt out of the room."

        print "\nWhat do you do?"
        print "1) say \"Sir, I am", player.name, "\b, and I am here to get some fairy dust for by bundt cake."
        print "2) say \"Look lizard breath, hand over the fairy dust or I'll wipe the walls with ya."
        print "3) run out of the room!"

        choice = functions.get_choice(3)

        #A bit of fun in a covertsation, all paths lead to the battle, with is outside all the if statements.
        if choice == 1:
            print "First you must do a small errand for me, little one."
            print "\nWhat do you say?"
            print "1) What is it you want?"
            print "2) Forget it you bird brain, hand over the stuff."

            choice2 = functions.get_choice(2)

            if choice == 1:
                print "The room reverberates with his low, evil chuckling.  \"You must return to me the rod"
                print "of evil evilness, held by the Priestess of Ultimate Bad Guys.  With that rod I can"
                print "enslave all of Fairy Land, and then I, Foul Lizard of Antioch, will win the annual"
                print "cook off with my rasberry lemon bars of pure evil!"

                print "\nThere's no way you can let the lizard beat you at the bake off!  You get your weapons"
                print "ready and charge in to the fight!"

            else:
                print "\"Never, you impertan-, impertin, impartantant, you stupid fool!  I will knock you down!\""
                print "the creature screams at you.  Time to fight!"

        else:
            print "\"Never, you little pixie wimp!  You will feel the might of my candy club!"

        fight = engines.CombatEngine()
        results = fight.fight(player, boss)

        if results == 'Victory':
            print "With a last strike from you", player.equiped_weapon[0].name, "the mighty lizard falls to"
            print "the earth, and crawls from the room into his fire pit santuary.  Looking about"
            print "the room you find a basin full of magic fairy dust!  You quickly fill your pouch"
            print "with enough for your recepie, and after a final look around the evil smelling"
            print "room, you depart for your kitchen.  At long last, all of Fairy Land will soon"
            print "know the supreme deliciousness of your budndt cake!"
            return 'Finished'

        else:
            print "Staggering from the lizard's monser blows, you run from the room at the last"
            print "moment, determined to come back and try again."
            return 'MonsterTwo'

#The map contains all the rooms from this map.  This is done here so that other maps
#can be easily substituted
class Map(object):
    rooms = { 'Prologue': Prologue(), 'Enterence' : Enterence(), 'MainHall' : MainHall(),
                'MonsterOne' : MonsterOne(), 'MonsterTwo' : MonsterTwo(),
                'PuzzleOne' : PuzzleOne(), 'Boss' : Boss(), 
                'Error' : 'Error', 'Finished' : 'Finished'}
