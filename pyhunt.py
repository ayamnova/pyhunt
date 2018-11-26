class Place:
    def __init__(self,desc,a_msg="",a_game_ends=False):
        self.description = desc
        self.destinations = dict()
        self.arrive_message = a_msg
        self.arrive_game_ends = a_game_ends

    def add_destination(self, direction, place):
        self.destinations[direction] = place

    def path(self, direction):
        if direction in self.destinations.keys():
            return(self.destinations[direction])
        else:
            return(None)

    def arrive(self):
        print(self.arrive_message)
        return(self.arrive_game_ends)

    def get_game_end(self):
        return self.arrive_game_ends

#instantiate all the places
valley = Place(
    desc="You are in a pleasant valley, with a trail ahead."
    )
path = Place(
    desc="You are on a path, with ravines on both sides."
    )
cliff = Place(
    desc="You are teetering on the edge of a cliff.",
    a_msg="You fall and die.",
    a_game_ends=True
    )
fork = Place(
    desc="You are at a fork in the path."
    )
maze_0 = Place(
    desc="You are in a maze of twisty trails, all alike."
    )
maze_1 = Place(
    desc="You are in a maze of twisty trails, all alike."
    )
maze_2 = Place(
    desc="You are in a maze of twisty trails, all alike."
    )
maze_3 = Place(
    desc="You are in a maze of twisty trails, all alike.",
    a_msg="An ogre sucks your brain out through your eye sockets"+
    " and you die.",
    a_game_ends=True
    )
mountaintop = Place(
    desc="You are on the mountaintop.",
    a_msg="There is treasure here.\nCongratulations! You win!",
    a_game_ends=True
    )

#connect all the destinations
valley.add_destination("forward",path)
path.add_destination("right",cliff)
path.add_destination("left",cliff)
path.add_destination("forward",fork)
fork.add_destination("left",maze_0)
fork.add_destination("right",mountaintop)
maze_0.add_destination("left", maze_1)
maze_0.add_destination("right", maze_3)
maze_1.add_destination("left", maze_0)
maze_1.add_destination("right", maze_2)
maze_2.add_destination("left", fork)
maze_2.add_destination("right", maze_0)
maze_3.add_destination("left", maze_0)
maze_3.add_destination("right", maze_3)

dir_arr = ["left","right","forward"]

def player():
    report(valley)

def report(location):
    print(location.description)
    if(location.arrive_message != ""):
        print(location.arrive_message)
    move(location)
    report

def move(x):
    if(x == valley):
        print("Directions:", dir_arr[2])
        dir_input = input("What direction? ")
        if(dir_input) == "forward":
            report(path)
        else:
            print("Not a possible direction")
    elif(x == path):
        print("Directions:", dir_arr)
        dir_input = input("What direction? ")
        if(dir_input) == "left":
            report(cliff)
        elif(dir_input) == "right":
            report(cliff)
        elif(dir_input) == "forward":
            report(fork)
        else:
            print("Not a possible direction")
    elif(x == cliff):
        Place.get_game_end = True
    elif(x == fork):
        print("Directions:",dir_arr[0:2])
        dir_input = input("What direction? ")
        if(dir_input) == "left":
            report(maze_0)
        elif(dir_input) == "right":
            report(mountaintop)
        else:
            print("Not a possible direction")
    elif(x == maze_0):
        print("Directions:",dir_arr[0:2])
        dir_input = input("What direction? ")
        if(dir_input) == "left":
            report(maze_1)
        else:
            report(maze_3)
    elif(x == maze_1):
        print("Directions:",dir_arr[0:2])
        dir_input = input("What direction? ")
        if(dir_input) == "left":
            report(maze_0)
        else:
            report(maze_2)
    elif(x == maze_2):
        print("Directions:",dir_arr[0:2])
        dir_input = input("What direction? ")
        if(dir_input) == "left":
            report(fork)
        else:
            report(maze_0)

def main():
    while(Place.get_game_end != True):
        player()
        Place.get_game_end = True
    print("Game Over")
    rest_input = input("Would you like to play again? \nY/N")
    if(rest_input.lower() == "y"):
        Place.get_game_end = False
        main()
    else:
        print("Thank you for playing!")

main()