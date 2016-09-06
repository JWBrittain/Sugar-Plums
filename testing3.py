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

        shield = objects.MagicShield()
        player.inventory.append(shield)
        player.equip_armor(shield)


        player.max_hit_points = 50
        player.hit_points = 50
        player.heal_potions = 40

        room = map_one.rooms['MonsterTwo']

        while room != 'Finished':
            next_room = room.enter(player)
            room = map_one.rooms[next_room]

game = Engine()
game.game()
