import unittest
from piggame.die import Die
from piggame.player import Player
from piggame.game import Game


class TestDie(unittest.TestCase):
    def test_roll_within_range(self):
        die = Die(seed=0)
        for _ in range(100):
            self.assertTrue(1 <= die.roll() <= 6)


class TestPlayer(unittest.TestCase):
    def test_add_score(self):
        p = Player("Andrew")
        p.add_score(10)
        self.assertEqual(p.score, 10)


class TestGame(unittest.TestCase):
    def test_multiple_players_initialization(self):
        g = Game("Alice", "Bob", "Charlie")
        self.assertEqual(len(g.players), 3)
        self.assertEqual(g.players[0].name, "Alice")


if __name__ == "__main__":
    unittest.main()
