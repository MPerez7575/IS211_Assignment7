from piggame.die import Die
from piggame.player import Player


WINNING_SCORE = 100


class Game:
    """Controls the flow and rules of the Pig Game."""

    def __init__(self, *player_names: str) -> None:
        """
        Initialize the game with one or more players.

        Args:
            *player_names: Any number of player names.
        """
        self.die = Die(seed=0)
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0

    def switch_player(self) -> None:
        """Switch turn to the next player (circular order)."""
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_current_player(self) -> Player:
        """Return the current player object."""
        return self.players[self.current_player_index]

    def play_turn(self, player: Player) -> None:
        """Play a single turn for the given player."""
        turn_total = 0
        print(f"\n{player.name}'s turn (Current score: {player.score})")

        while True:
            decision = input("Roll or hold? (r/h): ").strip().lower()
            if decision not in ("r", "h"):
                print("❌ Invalid input. Please enter 'r' or 'h'.")
                continue

            if decision == "r":
                roll = self.die.roll()
                print(f"🎲 {player.name} rolled a {roll}")

                if roll == 1:
                    print("💀 You rolled a 1! No points this turn.")
                    turn_total = 0
                    break

                turn_total += roll
                print(f"Turn total: {turn_total}, Potential total: {player.score + turn_total}")
            else:
                player.add_score(turn_total)
                print(f"✅ {player.name} holds. Total score: {player.score}")
                break

    def check_winner(self) -> bool:
        """Check if the current player has reached the winning score."""
        player = self.get_current_player()
        if player.score >= WINNING_SCORE:
            print(f"\n🏆 {player.name} wins with {player.score} points! 🏆")
            return True
        return False

    def reset_game(self) -> None:
        """Reset all player scores for a new game."""
        for player in self.players:
            player.reset()
        self.current_player_index = 0

    def play(self) -> None:
        """Main game loop."""
        print("🎮 Welcome to the Pig Dice Game! First to 100 wins!\n")

        while True:
            player = self.get_current_player()
            self.play_turn(player)

            if self.check_winner():
                again = input("\nPlay again? (y/n): ").strip().lower()
                if again == "y":
                    self.reset_game()
                    print("\n🔄 Starting a new game!\n")
                    continue
                else:
                    print("\n👋 Thanks for playing Pig Dice Game!")
                    break

            self.switch_player()
