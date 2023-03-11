import random
from abc import ABC, abstractmethod

class RandomCard(ABC):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __str__(self):
        return self.name

    def draw_card(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

    def shuffle(self):
        random.shuffle(self.cards)

    @abstractmethod
    def perform_action(self, player):
        pass

class CommunityChest(RandomCard):
    def __init__(self):
        super().__init__("Community Chest")
        self.cards = ["Advance to Go (Collect $200)", "Bank error in your favor – Collect $75", 
                      "Doctor's fees – Pay $50", "Get out of jail free – This card may be kept until needed", 
                      "Go to jail – Go directly to jail – Do not pass Go, do not collect $200", 
                      "Grand Opera Night – Collect $50 from every player for opening night seats", 
                      "Income Tax refund – Collect $20", "It is your birthday - Collect $10 from each player", 
                      "Life Insurance Matures – Collect $100", "Pay Hospital Fees of $100", 
                      "Pay School Fees of $50", "Receive $25 Consultancy Fee", 
                      "You are assessed for street repairs – $40 per house, $115 per hotel", 
                      "You have won second prize in a beauty contest– Collect $10", 
                      "You inherit $100"]

    def perform_action(self, player):
        card = self.draw_card()
        if card == "Advance to Go (Collect $200)":
            player.position = 0
            player.receive_money(200)
        elif card == "Bank error in your favor – Collect $75":
            player.receive_money(75)
        elif card == "Doctor's fees – Pay $50":
            player.pay_money(50)
        elif card == "Get out of jail free – This card may be kept until needed":
            player.add_card(self, card)
        elif card == "Go to jail – Go directly to jail – Do not pass Go, do not collect $200":
            player.go_to_jail()
        elif card == "Grand Opera Night – Collect $50 from every player for opening night seats":
            for other_player in player.game.players:
                if other_player != player:
                    player.pay_money_to_other_player(50, other_player)
        elif card == "Income Tax refund – Collect $20":
            player.receive_money(20)
        elif card == "It is your birthday - Collect $10 from each player":
            for other_player in player.game.players:
                if other_player != player:
                    player.pay_money_to_other_player(10, other_player)
        elif card == "Life Insurance Matures – Collect $100":
            player.receive_money(100)
        elif card == "Pay Hospital Fees of $100":
            player.pay_money(100)
        elif card == "Pay School Fees of $50":
            player.pay_money(50)
        elif card == "Receive $25 Consultancy Fee":
            player.receive_money(25)
        elif card == "You are assessed for street repairs – $40 per house, $115 per hotel":
            total_cost = 0
            for property_card in player.properties:
                if property_card.houses == 5:
                    total_cost += 115
                else:
                    break

class Chance(RandomCard):
    def __init__(self):
        super().__init__("Chance")
        self.cards = ["Advance to Go (Collect $200)", "Advance to Illinois Ave. – If you pass Go, collect $200", 
                      "Advance to St. Charles Place – If you pass Go, collect $200", "Advance to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.", 
                      "Advance to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.", "Bank pays you dividend of $50", 
                      "Get out of Jail Free – This card may be kept until needed, or sold", "Go Back 3 Spaces", 
                      "Go to Jail – Go directly to Jail – Do not pass Go, do not collect $200", "Make general repairs on all your property – For each house pay $25 – For each hotel $100", 
                      "Pay poor tax of $15", "Take a trip to Reading Railroad – If you pass Go, collect $200", 
                      "Take a walk on the Boardwalk – Advance to Boardwalk", "You have been elected Chairman of the Board – Pay each player $50", 
                      "Your building and loan matures – Collect $150", "You have won a crossword competition - Collect $100"]

    def perform_action(self, player):
        card = self.draw_card()
        if card == "Advance to Go (Collect $200)":
            player.position = 0
            player.receive_money(200)
        elif card == "Advance to Illinois Ave. – If you pass Go, collect $200":
            if player.position > 24:
                player.receive_money(200)
            player.position = 24
        elif card == "Advance to St. Charles Place – If you pass Go, collect $200":
            if player.position > 11:
                player.receive_money(200)
            player.position = 11
        elif card == "Advance to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times the amount thrown.":
            if player.position < 12 or player.position > 28:
                player.position = 12
            elif player.position < 28:
                player.position = 28
            if player.game.board[player.position].owner is not None:
                player.pay_rent()
            else:
                player.game.auction_property(player.game.board[player.position])
        elif card == "Advance to the nearest Railroad and pay owner twice the rental to which he/she is otherwise entitled. If Railroad is unowned, you may buy it from the Bank.":
            if player.position < 5:
                player.position = 5
            elif player.position < 15:
                player.position = 15
            elif player.position < 25:
                player.position = 25
            elif player.position < 35:
                player.position = 35
            railroad = player.game.board[player.position]
            if railroad.owner is not None:
                rent = railroad.get_rent()
                player.pay_rent(rent*2)
            else:
                player.game.auction_property(railroad)
        elif card == "Bank pays you dividend of $50":
            player.receive_money(50)
        elif card == "Get out of Jail Free – This card may be kept until needed, or sold":
            player.add_card(self, card)
        elif card == "Go Back 3 Spaces":
            player.position -= 3
           
