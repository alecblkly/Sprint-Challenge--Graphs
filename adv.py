from room import Room
from player import Player
from world import World
from util import Stack, Queue
import pprint

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
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
# Commands that might be useful are:
# player.current_room.id
# player.current_room.get_exits()
# player.travel(direction)
print("Current_room.id: ", player.current_room.id)
print("Current_room.get_exits: ", player.current_room.get_exits())
# If we move from room X north, then we know there is a room south of the new room
# We would then be able to change the "?" value to the room_id
# Want to traverse the maze so all "?" values contain a room_id
# If there are no more "?", then we know we've been to all rooms
print("length - room_graph: ", len(room_graph))
print("length - traversal_path: ", len(traversal_path))
print(f"room_graph: \n{pprint.pformat(room_graph)}")
# You're able to get a length of the room_graph
# traversal_path is going to be a list of all directions to traverse maze
# Which you would also be able to check a length of
# Check if the traversal_path has a smaller length than room_graph
# If the traversal_path is smaller, then a loop of movement would occur


class Graph:
    def __init__(self):
        self.vertices = {}

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("ERROR: Vertex does not exist.")

    # Working on DFT per hint in spec
    def maze_traversal(self, starting_point):
        # Create a stack
        s = Stack()
        # Push the starting point, which is going to be 0
        s.push(starting_point)
        # Create a set to store visited
        visited = set()
        # While stack is not empty
        while s.size > 0:
            # Setting variables
            # -----------------
            # Current_room defined by id
            current_room = player.current_room.id
            # Adding current room id to visited set
            visited.add(current_room)
            # Rooms that haven't be visited
            not_visited = {}
            # If the length of the traversal path is less than the length of the room_graph
            if len(traversal_path) < len(room_graph):
                pass

    # Working on BFS per hint in spec
    def shortest_path(self, starting_point, destination_point):
        pass


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
