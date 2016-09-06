import characters

class Weapon(object):
    pass

class RainbowSparkleSword(Weapon):

    name = "Rainbow Sparkle Sword"

    attack_power = 15 
    attack_chance = 15 

class SparkleGlitterBlaster(Weapon):

    name = "Sparkle Glitter Blaster"

    attack_power = 20 
    attack_chance = 20 

class ShimmerDagger(Weapon):
    name = "Shimmer Dagger"

    attack_power = 10
    attack_chance = 10

class BareHands(Weapon):

    name = "Bare Hands"

    attack_power = 5
    attack_chance = 5 

class Armor(object):
    pass

class NoArmor(Armor):
    
    name = "No Armor"
    armor = 0
    dodge_penalty = 0 

class MagicShield(Armor):

    name = "Magic Shield"
    armor = 5
    dodge_penalty = 2

class BreastPlate(Armor):

    name = "Breat Plate"
    armor = 10
    dodge_penalty = 5

