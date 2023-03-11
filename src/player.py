class Player:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.properties = []
        self.current_position = 0
        self.is_in_jail = False
        self.num_jail_cards = 0
        self.num_railroads_owned = 0
        self.num_utilities_owned = 0
        self.num_double_rolls = 0

    def __str__(self):
        return f"{self.name} (${self.balance})"

    def get_balance(self):
        return self.balance

    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        self.balance -= amount

    def add_property(self, property_card):
        self.properties.append(property_card)
        property_card.set_owner(self)
        if isinstance(property_card, RailroadCard):
            self.num_railroads_owned += 1
        elif isinstance(property_card, UtilityCard):
            self.num_utilities_owned += 1

    def remove_property(self, property_card):
        self.properties.remove(property_card)
        property_card.set_owner(None)
        if isinstance(property_card, RailroadCard):
            self.num_railroads_owned -= 1
        elif isinstance(property_card, UtilityCard):
            self.num_utilities_owned -= 1

    def get_properties(self):
        return self.properties

    def get_current_position(self):
        return self.current_position

    def set_current_position(self, position):
        self.current_position = position

    def move(self, num_spaces):
        self.current_position += num_spaces
        if self.current_position > 39:
            self.current_position -= 40
            self.add_balance(200)

    def go_to_jail(self):
        self.current_position = 10
        self.is_in_jail = True

    def get_is_in_jail(self):
        return self.is_in_jail

    def get_num_jail_cards(self):
        return self.num_jail_cards

    def add_jail_card(self):
        self.num_jail_cards += 1

    def remove_jail_card(self):
        if self.num_jail_cards > 0:
            self.num_jail_cards -= 1

    def get_num_railroads_owned(self):
        return self.num_railroads_owned

    def get_num_utilities_owned(self):
        return self.num_utilities_owned

    def add_double_roll(self):
        self.num_double_rolls += 1

    def reset_double_rolls(self):
        self.num_double_rolls = 0

    def get_num_double_rolls(self):
        return self.num_double_rolls
