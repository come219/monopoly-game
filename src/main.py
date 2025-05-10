# main py for monopoly game



#inits everything

# then calls game object

# not monopoly game object
# not menu system object
# not httpservice object


import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500

    def move(self, steps, board_size):
        self.position = (self.position + steps) % board_size
        print(f"{self.name} moved to position {self.position}.")

    def adjust_money(self, amount):
        self.money += amount
        print(f"{self.name} now has ${self.money}.")

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    print("Welcome to Monopoly MVP!")

    board = ["GO", "Mediterranean Ave", "Community Chest", "Baltic Ave", "Income Tax", "Reading Railroad"]
    players = [Player("Player 1"), Player("Player 2")]
    current_turn = 0

    while True:
        player = players[current_turn]
        input(f"\n{player.name}'s turn. Press Enter to roll the dice...")
        dice = roll_dice()
        print(f"{player.name} rolled a {dice}.")
        player.move(dice, len(board))

        # Example action on a space
        current_space = board[player.position]
        print(f"{player.name} landed on {current_space}.")
        if current_space == "Income Tax":
            player.adjust_money(-200)
        elif current_space == "GO":
            player.adjust_money(200)

        # Switch to next player
        current_turn = (current_turn + 1) % len(players)

        # Optional: add a basic exit condition
        if any(p.money <= 0 for p in players):
            print("\nGame over!")
            for p in players:
                print(f"{p.name} - ${p.money}")
            break

if __name__ == "__main__":
    main()
