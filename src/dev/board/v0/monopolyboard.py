from classic_version import Classic
from us_version import US
from worldedition_version import WorldEdition

class MonopolyBoard:
    def __init__(self):
        self.spaces = []
        self.property_names = {}

    def add_space(self, space):
        self.spaces.append(space)

    def display_map(self):
        for i in range(len(self.spaces)):
            print("{}: {}".format(i, self.spaces[i]))

    def get_property_name(self, property_num):
        return self.property_names.get(property_num, "Unknown Property")

    def create_board(self, version):
        if version == "World Edition":
            board = WorldEdition()
        elif version == "Classic":
            board = Classic()
        elif version == "US":
            board = US()
        else:
            board = MonopolyBoard()
        self.spaces = board.spaces
        self.property_names = board.property_names

    def __str__(self):
        return "Monopoly board with {} spaces".format(len(self.spaces))



board = MonopolyBoard()

# Create and display the Classic version map
board.create_board("Classic")
board.display_map()

# Create and display the US version map
board.create_board("US")
board.display_map()

# Create and display the World Edition version map
#board.create_board("World Edition")
#board.display_map()
