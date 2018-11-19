class Place(object):
    def __init__(self, desc, a_msg="", a_game_ends=False):
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


def setup():
    # Instantiate all the places
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
            a_msg="An ogre sucks your brain out through your eye sockets" +
            " and you die.",
            a_game_ends=True
            )
    mountaintop = Place(
            desc="You are on the mountaintop.",
            a_msg="There is treasure here.\nCongratulations! You Win!",
            a_game_ends=True
            )

    # Connect all the destinations
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

if __name__ == '__main__':
    setup()
