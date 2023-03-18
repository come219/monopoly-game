class TradingSystem:
    def __init__(self):
        self.offers = []
        self.trades = []

    def see_offers(self):
        print("\nCurrent offers:")
        for offer in self.offers:
            print(offer)

    def see_trades(self):
        print("\nRecent trades:")
        for trade in self.trades:
            print(trade)

    def create_offer(self):
        stock = input("Enter stock name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        offer = {"stock": stock, "price": price, "quantity": quantity}
        self.offers.append(offer)
        print("Offer created successfully.")

    def see_trade_history(self):
        print("\nTrade history:")
        for trade in self.trades:
            print(trade)

    def exit(self):
        print("Exiting trading system.")
        quit()

    def run(self):
        while True:
            print("\nWelcome to the trading system!")
            print("1. See offers")
            print("2. See trades")
            print("3. Create offer")
            print("4. See trade history")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.see_offers()
            elif choice == "2":
                self.see_trades()
            elif choice == "3":
                self.create_offer()
            elif choice == "4":
                self.see_trade_history()
            elif choice == "5":
                self.exit()
            else:
                print("Invalid choice. Try again.")
trading_system = TradingSystem()
trading_system.run()
