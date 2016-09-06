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
                    print "You take a deep breath and check your items, then step through the final door"
                    print "of the dungeon."
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
    
    def enter(self, player):
        print "We are in puzzle room 1"
        return 'Finished'

class Boss(Room):

    def enter(self, player):

        boss = functions.boss_packer(1) 

        print "<BOSS DESCRIPTION>"
        print "<BOSS CONVERSATION?>"

        fight = engines.CombatEngine()
        results = fight.fight(player, boss)

        if results == 'Victory':
            print "Yay you won!"
        else:
            print "Dang! You run from the room at the last moment, determined to come back and try again."
            return 'MonsterTwo'


        

#The map contains all the rooms from this map.  This is done here so that other maps
#can be easily substituted
class Map(object):
    rooms = { 'Prologue': Prologue(), 'Enterence' : Enterence(), 'MainHall' : MainHall(),
                'MonsterOne' : MonsterOne(), 'MonsterTwo' : MonsterTwo(),
                'PuzzleOne' : PuzzleOne(), 'Boss' : Boss(), 
                'Error' : 'Error', 'Finished' : 'Finished'}
