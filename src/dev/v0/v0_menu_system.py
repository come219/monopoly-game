class MonopolyMenu:
    def __init__(self):
        self.mode = "Singleplayer"  # default game mode is singleplayer

    def classic_game(self):
        # code to start classic Monopoly game
        print("Starting classic Monopoly game... (Mode: {})".format(self.mode))

    def fast_version(self):
        # code to start fast version Monopoly game
        print("Starting fast version Monopoly game... (Mode: {})".format(self.mode))

    def options(self):
        # code to show options menu
        print("Options menu:")
        print("1. Change game settings")
        print("2. View game instructions")
        print("3. Change game mode")
        print("4. Return to main menu")

        option = input("Enter an option number: ")
        if option == "1":
            # code to change game settings
            print("Changing game settings... (Mode: {})".format(self.mode))
        elif option == "2":
            # code to view game instructions
            print("Viewing game instructions... (Mode: {})".format(self.mode))
        elif option == "3":
            # code to change game mode
            print("Game modes:")
            print("1. Singleplayer")
            print("2. Multiplayer")
            print("3. Localhost")
            print("4. Online")

            mode = input("Enter a game mode number: ")
            if mode == "1":
                self.mode = "Singleplayer"
                print("Switching to singleplayer mode... (Mode: {})".format(self.mode))
            elif mode == "2":
                self.mode = "Multiplayer"
                print("Switching to multiplayer mode... (Mode: {})".format(self.mode))
            elif mode == "3":
                self.mode = "Localhost"
                print("Switching to localhost mode... (Mode: {})".format(self.mode))
            elif mode == "4":
                self.mode = "Online"
                print("Switching to online mode... (Mode: {})".format(self.mode))
            else:
                print("Invalid mode number. Returning to options menu... (Mode: {})".format(self.mode))
        elif option == "4":
            # return to main menu
            print("Returning to main menu... (Mode: {})".format(self.mode))
        else:
            print("Invalid option. Returning to main menu... (Mode: {})".format(self.mode))

    def run(self):
        while True:
            print("Monopoly menu:")
            print("1. Classic game")
            print("2. Fast version")
            print("3. Options")
            print("4. Exit")

            choice = input("Enter a menu option number: ")
            if choice == "1":
                self.classic_game()
            elif choice == "2":
                self.fast_version()
            elif choice == "3":
                self.options()
            elif choice == "4":
                print("Exiting Monopoly game. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

menu = MonopolyMenu()
menu.run()
