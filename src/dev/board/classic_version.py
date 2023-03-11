#from monopolyboard import MonopolyBoard

class Classic(MonopolyBoard):
    def __init__(self):
        super().__init__()
        self.add_space("Go")
        for i in range(1, 40):
            if i in [5, 15, 25, 35]:
                self.add_space("Income Tax")
            elif i in [12, 28]:
                self.add_space("Utility")
                if i == 12:
                    self.property_names["Utility"] = "Electric Company"
                else:
                    self.property_names["Utility"] = "Water Works"
            elif i in [8, 23, 37]:
                self.add_space("Chance")
            elif i in [11, 21, 31]:
                self.add_space("Community Chest")
            elif i == 19:
                self.add_space("Free Parking")
            elif i == 39:
                self.add_space("Go to Jail")
            elif i == 4:
                self.add_space("Income Tax")
            elif i == 38:
                self.add_space("Luxury Tax")
            else:
                property_name = "Property {}".format(i)
                self.add_space(property_name)
                self.property_names[property_name] = "Classic Property {}".format(i)
