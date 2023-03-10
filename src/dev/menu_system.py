class MonopolyMenu:
    def __init__(self):
        self.mode = "Singleplayer"  # default game mode is singleplayer

    def classic_game(self):
        # code to start classic Monopoly game
        print("Starting classic Monopoly game... (Mode: {})".format(self.mode))

    def fast_version(self):
        # code to start fast version Monopoly game
        print("Starting fast version Monopoly game... (Mode: {})".format(self.mode))

    def multi_region(self):
	# code to start multi region monopoly game that will be a test dev for lstand ...
	# railroads or airports lead to portals to different regions (?)
	# idk, multi monopoly maps that connect with each other ...
        print("starting multi-region test monopoly")


    def options(self):
        # code to show options menu
        print("Options menu:")
        print("1. Change game settings")
        print("2. View game instructions")
        print("3. Change game mode")
        print("4. Configure Bots")
        print("5. Return to main menu")

        option = input("Enter an option number: ")
        if option == "1":
            # code to change game settings
            print("Changing game settings... (Mode: {})".format(self.mode))
        elif option == "2":
            # code to view game instructions
2            print("Viewing game instructions... (Mode: {})".format(self.mode))
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
                # configure bots
                print("Bot configuration menu:")
                print("1. Change number of bots")
                print("2. Change bot difficulty")
                print("3. Return to options menu")

                bot_option = input("Enter an option number: ")
                if bot_option == "1":
                    # change number of bots
                    num_bots = input("Enter the number of bots (0-3): ")
                    if num_bots.isdigit() and 0 <= int(num_bots) <= 3:
                        self.num_bots = int(num_bots)
                        print("Number of bots set to {}. (Mode: {})".format(self.num_bots, self.mode))
                    else:
                        print("Invalid number of bots. Please enter a number between 0 and 3.")
                elif bot_option == "2":
                    # change bot difficulty
                    print("Bot difficulties:")
                    print("1. Easy")
                    print("2. Medium")
                    print("3. Hard")

                    difficulty_option = input("Enter a difficulty number: ")
                    if difficulty_option == "1":
                    self.bot_difficulty = "Easy"
                    print("Bot difficulty set to {}. (Mode: {})".format(self.bot_difficulty, self.mode))
                elif difficulty_option == "2":
                    self.bot_difficulty = "Medium"
                    print("Bot difficulty set to {}. (Mode: {})".format(self.bot_difficulty, self.mode))
                elif difficulty_option == "3":
                    self.bot_difficulty = "Hard"
                    print("Bot difficulty set to {}. (Mode: {})".format(self.bot_difficulty, self.mode))
                else:
                    print("Invalid difficulty number. Returning to bot configuration menu... (Mode: {})".format(self.mode))
            elif bot_option == "3":
                # return to options menu
                pass
        else:
            print("Invalid option number. Returning to options menu... (Mode: {})".format(self.mode))

	elif option == "5":
            # return to main menu
            print("Returning to main menu... (Mode: {})".format(self.mode))
        else:
            print("Invalid option. Returning to main menu... (Mode: {})".format(self.mode))
2
    def run(self):
        while True:
            print("Monopoly menu:")
            print("1. Classic game")
            print("2. Fast version")
	    print("3. Multi-region game")
            print("4. Options")
            print("5. Exit")

            choice = input("Enter a menu option number: ")
            if choice == "1":
                self.classic_game()
            elif choice == "2":
                self.fast_version()
	    elif choice == "3":
	        self.multi_region()
            elif choice == "4":
                self.options()
            elif choice == "5":
                print("Exiting Monopoly game. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

menu = MonopolyMenu()
menu.run()
