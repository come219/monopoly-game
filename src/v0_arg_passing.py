import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Play Monopoly game")
    parser.add_argument('--difficulty', type=str, default='easy', help='Set game difficulty')
    parser.add_argument('--http-endpoint', type=str, default='http://localhost:8080', help='Set HTTP service endpoint')

    args = parser.parse_args()

    # create objects with arguments
    menu = MonopolyMenu(difficulty=args.difficulty)
    game = MonopolyGame(difficulty=args.difficulty)
    http_service = HTTPService(endpoint=args.http_endpoint)

    # call methods
    menu.display_menu()
    game.play()
    http_service.get_data()

