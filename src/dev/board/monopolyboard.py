class MonopolyBoardFactory:
    BOARD_SIZES = {"standard": 40, "short": 20}

    def create_board(self, board_type="standard", players=None):
        if players is None:
            players = []
        board_size = self.BOARD_SIZES.get(board_type, self.BOARD_SIZES["standard"])
        return MonopolyBoard(players, board_size)


import csv

class MonopolyBoard:
    def __init__(self, players, board_file):
        self.players = players
        self.current_player = 0
        self.board = self.create_board(board_file)

    def create_board(self, board_file):
        board = []
        with open(board_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                square_type = row['Type']
                if square_type == 'Go':
                    square = Square(row['Name'], int(row['Reward']))
                elif square_type == 'Property':
                    square = PropertySquare(row['Name'], int(row['Price']), int(row['Rent']), int(row['Mortgage']), int(row['HouseCost']), int(row['Rent1']), int(row['Rent2']), int(row['Rent3']), int(row['Rent4']), int(row['Rent5']))
                elif square_type == 'Railroad':
                    square = RailroadSquare(row['Name'], int(row['Price']))
                else:
                    square = Square(row['Name'], int(row['Penalty']))
                board.append(square)
        return board

    def play_turn(self):
        current_player = self.players[self.current_player]
        current_square = self.board[current_player.position]
        current_square.land_on(current_player)
        self.current_player = (self.current_player + 1) % len(self.players)
