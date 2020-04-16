from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Importing stack and queue
from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# NOTE: Notes from spec
# Start with a DFT - Pick unexplored direction, travels to that direction and loops
# Once a dead-end occurs, move to a room with an unexplored path

while len(traversal_path) < len(room_graph):
    unvisited_rooms = {}
    # Finding directions for exits of the current room
    for directions in player.current_room.get_exits():
        # Want to traverse to a new room - player.travel(direction)
        # Want to store which room we moved to
        print(directions)
        # To find the shortest path to an unexplored room, utilize BFS
        # Convert room ids to n/s/e/w directions

        # DFT is able to travel throughout the map, BFS is able to find the shortest path
        # Combining the DFT and BFS, would enable for traveling throughout the map on the shortest path
        # This would be sent into traversal_path (Return)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
