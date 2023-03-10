import logging

def main() -> None:
    logging.basicConfig(filename='monopoly.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
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
        logging.error(f"An error occurred: {e}")

