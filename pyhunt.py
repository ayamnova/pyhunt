class Place:
    def __init__(self, desc, a_msg="", a_game_ends=False):
        self.description = desc
        self.destinations = dict()
        self.arrive_message = a_msg
        self.arrive_game_ends = a_game_ends

    def add_destination(self, direction, place):
        self.destinations[direction] = place

    def get_place(self, direction):
        if direction in self.destinations.keys():
            return(self.destinations[direction])
        else:
            return(None)

    def get_directions(self):
        return (list(self.destinations.keys()))

    def arrive(self):
        # Only print information if something special happens
        if self.arrive_message != "":
            print(self.description)
            print(self.arrive_message)

    def get_game_end(self):
        return self.arrive_game_ends


class Player():
    def __init__(self, place):
        self.location = place

    def move(self, direction):
        self.location = self.location.get_place(direction)


def report(location):
    print(location.description)
    print("You can go: " + ", ".join(location.get_directions()))


def main():
    player = Player(valley)
    while True:
        report(player.location)
        #  Get a valid direciton
        inp = input("Where would you like to go: ")
        while inp not in player.location.get_directions():
            print("That was not a valid direction!\n")
            report(player.location)
            inp = input("Where would you like to go: ")

        # Move
        player.move(inp)
        player.location.arrive()

        # Check if the game ends
        if player.location.get_game_end() is True:
            break

    rest_input = input("\nWould you like to play again? \nY/N: ")
    if(rest_input.lower() == "y"):
        main()
    else:
        print("Thank you for playing!")


if __name__ == '__main__':
    # instantiate all the places
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

    # connect all the destinations
    valley.add_destination("forward", path)
    path.add_destination("right", cliff)
    path.add_destination("left", cliff)
    path.add_destination("forward", fork)
    fork.add_destination("left", maze_0)
    fork.add_destination("right", mountaintop)
    maze_0.add_destination("left", maze_1)
    maze_0.add_destination("right", maze_3)
    maze_1.add_destination("left", maze_0)
    maze_1.add_destination("right", maze_2)
    maze_2.add_destination("left", fork)
    maze_2.add_destination("right", maze_0)
    maze_3.add_destination("left", maze_0)
    maze_3.add_destination("right", maze_3)

    main()
