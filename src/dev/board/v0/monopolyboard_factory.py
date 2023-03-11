from classic_version import Classic
from us_version import US
from worldedition_version import WorldEdition

class MonopolyBoard:
    def __init__(self):
        self.spaces = []
        self.property_names = {}

    def add_space(self, space):
        self.spaces.append(space)

    def __str__(self):
        return "Monopoly board with {} spaces".format(len(self.spaces))


class MonopolyBoardFactory:
    @staticmethod
    def create_board(version):
        if version == "World Edition":
            board = WorldEdition()
        elif version == "Classic":
            board = Classic()
        elif version == "US":
            board = US()
        return board
