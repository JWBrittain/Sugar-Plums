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
import objects
import functions
import maps
import engines

class Engine(object):

    def game(self):

        map_one = maps.Map()
        player = characters.Player()

        player.name = "Ogoglio"

        print player.name

        dagger = objects.ShimmerDagger()
        player.inventory.append(dagger)
        player.equip_weapon(dagger)

        plate = objects.BreastPlate()
        player.inventory.append(plate)
        player.equip_armor(plate)

        shield = objects.MagicShield()
        player.inventory.append(shield)
        player.equip_armor(shield)


        player.max_hit_points = 50
        player.hit_points = 50
        player.heal_potions = 40

        room = map_one.rooms['PuzzleOne']

        while room != 'Finished':
            next_room = room.enter(player)
            room = map_one.rooms[next_room]

game = Engine()
game.game()
