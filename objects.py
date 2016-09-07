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

