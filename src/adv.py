from room import Room
from player import Player
from item import Item
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     items=[Item(name='Torch', description='A torch to guide your way')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items=[Item(name='Sword', description='This is a 1 hand sword'),
                                        Item(name='Mace', description='This is a 1 hand mace')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items=[Item(name='Axe',
                                                                    description='This is a 1h axe')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", items=[Item(name='Greatsword',
                                                               description='This is a 2 hand sword'),
                                                          Item(name='Shield', description='This is a shield')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

if __name__ == '__main__':

    p_name = input("Hello and welcome! Please enter your name:")
    player = Player(name=p_name, current_room=room['outside'])

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



    while True:
            print("--" * 20)
            print("Current room:", player.current_room.name)
            print("Room description:", player.current_room.description)
            print("Room items:", [item.name for item in player.current_room.items])

            player_input = input("Please enter a command:")
            player_input_first = player_input.split()[0]

            if player_input == "q":
                print("Exiting Game")
                sys.exit()

            if player_input == 'i' or player_input == 'inventory':
                print("Inventory:", [item.name for item in player.items])
                continue

            directional_commands = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}
            item_commands = ['get', 'drop', 'i', 'inventory']

            try:
                player.current_room = getattr(player.current_room, directional_commands[player_input_first.lower()])
                continue
            except AttributeError:
                if player_input_first not in item_commands:
                    print("Cannot go in that direction")
                    continue
            except KeyError:
                if player_input_first not in item_commands:
                    print("Invalid command!")
                    continue


            player_input_itemname = player_input.split()[1]
            p_item = None

            if player_input_first == 'get':
                for item in player.current_room.items:
                    if item.name == player_input_itemname:
                        p_item = item

                if p_item is not None:
                    player.items.append(p_item)
                    p_item.on_take()
                    player.current_room.remove_item(p_item)
            elif player_input_first == 'drop':
                for item in player.items:
                    if item.name == player_input_itemname:
                        p_item = item

                if p_item is not None:
                    player.items.remove(p_item)
                    p_item.on_drop()
                    player.current_room.add_item(p_item)
