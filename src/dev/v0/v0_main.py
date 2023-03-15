# main.py

from typing import Optional
from monopoly_menu import MonopolyMenu
from monopoly_game import MonopolyGame
from http_service import HTTPService

def main() -> None:
    """
    Entry point of the program.
    Creates objects of MonopolyMenu, MonopolyGame, and HTTPService classes, 
    and calls their respective methods to display the menu, play the game, and 
    retrieve data from an HTTP service.
    """
    try:
        # create objects
        menu = MonopolyMenu()
        game = MonopolyGame()
        http_service = HTTPService()

        # call methods
        menu.display_menu()
        game.play()
        http_service.get_data()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()


