# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your #scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for #Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a #draw, and 6 if you won).

from typing import List

mapping = {
    "rock": {"opponent": "A", "player": "X", "value": 1, "outcome": -1},
    "paper": {"opponent": "B", "player": "Y", "value": 2, "outcome": 1},
    "scissors": {"opponent": "C", "player": "Z", "value": 3, "outcome": 2},
}

LOST = 0
DRAW = 3
WIN = 6


class Solution:
    @staticmethod
    def get_input(path: str) -> List[str]:
        with open(path, "r") as file:
            return file.read().splitlines()

    @staticmethod
    def convert(match: str):
        opponent, player = match.split(" ")
        for key, value in mapping.items():
            if value["opponent"] == opponent:
                opponent = key
            if value["player"] == player:
                player = key
        return opponent, player

    def comparison(self, opponent: str, player: str) -> int:
        if opponent == player:
            return DRAW
        elif opponent == "rock" and player == "paper":
            return WIN
        elif opponent == "paper" and player == "scissors":
            return WIN
        elif opponent == "scissors" and player == "rock":
            return WIN
        else:
            return LOST

    def match_for_tactic(self, opponent: str, status: str) -> int:
        if status == "win":
            if opponent == "rock":
                return WIN + mapping["paper"]["value"]
            elif opponent == "paper":
                return WIN + mapping["scissors"]["value"]
            else:
                return WIN + mapping["rock"]["value"]
        elif status == "lost":
            if opponent == "rock":
                return LOST + mapping["scissors"]["value"]
            elif opponent == "paper":
                return LOST + mapping["rock"]["value"]
            else:
                return LOST + mapping["paper"]["value"]
        else:
            if opponent == "rock":
                return DRAW + mapping["rock"]["value"]
            elif opponent == "paper":
                return DRAW + mapping["paper"]["value"]
            else:
                return DRAW + mapping["scissors"]["value"]

    def tactic_comparison(self, opponent: str, player: str) -> int:
        outcome = mapping[player]["outcome"]
        if outcome == -1:
            return self.match_for_tactic(opponent, "lost")
        elif outcome == 1:
            return self.match_for_tactic(opponent, "draw")
        else:
            return self.match_for_tactic(opponent, "win")

    @staticmethod
    def task1():
        input = solution.get_input("input.txt")
        score = 0
        for match in input:
            opponent, player = solution.convert(match)
            score += mapping[player]["value"]
            score += solution.comparison(opponent, player)
        print(f"Score: {score}")

    @staticmethod
    def task2():
        input = solution.get_input("input.txt")
        score = 0
        for match in input:
            opponent, player = solution.convert(match)
            score += solution.tactic_comparison(opponent, player)
        print(f"Score: {score}")


if __name__ == "__main__":
    solution = Solution()
    solution.task1()
    solution.task2()
