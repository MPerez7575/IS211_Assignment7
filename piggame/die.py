import random

class Die:
    """Represents a six-sided die."""

    def __init__(self, seed: int = 0) -> None:
        random.seed(seed)

    def roll(self) -> int:
        """Return a random number between 1 and 6."""
        return random.randint(1, 6)
