"""
main.py
---------------------------------
Entry point for running the Pig Game with configurable players.
"""

import argparse
from piggame.game import Game


def main() -> None:
    """Initialize and start the Pig Game."""
    parser = argparse.ArgumentParser(description="Play the Pig Dice Game")
    parser.add_argument("--numPlayers", type=int, default=2, help="Number of players (default: 2)")
    args = parser.parse_args()

    # Create player names dynamically
    player_names = [f"Player {i + 1}" for i in range(args.numPlayers)]

    # Initialize and start the game
    game = Game(*player_names)
    game.play()


if __name__ == "__main__":
    main()
