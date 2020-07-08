from room import Room
from player import Player
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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
        print("Description:", player.current_room.description)

        direction = input("What way do you want to go? Choices(n, s, e, w):")

        if direction == "q":
            print("Quitting!")
            sys.exit()

        commands = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}

        try:
            player.current_room = getattr(player.current_room, commands[direction.lower()])
        except AttributeError:
            print("Cannot go in that direction")
            continue
        except KeyError:
            print("Invalid command!")
            continue
