class PropertyCard:
    def __init__(self, name, price, rent, color, mortgage_value, house_rent, hotel_rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.color = color
        self.mortgage_value = mortgage_value
        self.house_rent = house_rent
        self.hotel_rent = hotel_rent
        self.num_houses = 0
        self.num_hotels = 0
        self.is_mortgaged = False
        self.owner = None

    def __str__(self):
        return f"{self.name} (${self.price})"

    def get_rent(self):
        if self.num_hotels > 0:
            return self.hotel_rent
        elif self.num_houses > 0:
            return self.house_rent[self.num_houses-1]
        else:
            return self.rent

    def get_color(self):
        return self.color

    def get_mortgage_value(self):
        return self.mortgage_value

    def get_num_houses(self):
        return self.num_houses

    def get_num_hotels(self):
        return self.num_hotels

    def get_is_mortgaged(self):
        return self.is_mortgaged

    def get_owner(self):
        return self.owner

    def set_owner(self, player):
        self.owner = player

    def mortgage(self):
        self.is_mortgaged = True

    def unmortgage(self):
        self.is_mortgaged = False

    def add_house(self):
        if self.num_houses < 4:
            self.num_houses += 1

    def remove_house(self):
        if self.num_houses > 0:
            self.num_houses -= 1

    def add_hotel(self):
        if self.num_houses == 4:
            self.num_houses = 0
            self.num_hotels = 1

    def remove_hotel(self):
        if self.num_hotels == 1:
            self.num_hotels = 0
            self.num_houses = 4
