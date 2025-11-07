class Player:
    """Represents a player in the Pig Game."""

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.score: int = 0

    def add_score(self, points: int) -> None:
        self.score += points

    def reset(self) -> None:
        self.score = 0

    def __str__(self) -> str:
        return f"{self.name} (Score: {self.score})"
