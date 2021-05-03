from pathlib import Path
from typing import List, Optional
from pandas import DataFrame


class Quiz:

    def __init__(self, players: List[str], num_rounds: int = 5, round_length: int = 5):
        assert len(players) > 1, "Quiz must have at least 2 players."
        self.round_length = round_length
        self.__leaderboard = DataFrame(index=range(1, num_rounds + 1), columns=players)

    @property
    def players(self) -> List[str]:
        """Returns the list of players participating."""
        return self.__leaderboard.columns.tolist()

    @property
    def current_round(self) -> Optional[int]:
        """Returns the current active round in the Quiz, or None if the quiz has been completed."""
        unfinished_rounds = self.__leaderboard[self.__leaderboard.isna().any(axis=1)]
        if unfinished_rounds.empty:
            return None
        else:
            return unfinished_rounds.index[0]

    def __str__(self):
        df = self.full_leaderboard()
        return str(df)

    def add_score(self, player_name: str, score: int):
        """Adds given score for given player to the current active round
        @:raises KeyError if player_name is not a valid player
        @:raises ValueError if the score is not valid
        @:raises RuntimeError if the quiz has already ended."""
        if player_name not in self.__leaderboard.columns:
            raise KeyError(player_name)

        if not (0 <= score <= self.round_length):
            raise ValueError(f"Invalid score: {score}")

        if self.current_round is None:
            raise RuntimeError("Quiz is already finished!")

        self.__leaderboard.loc[self.current_round, player_name] = score

    def full_leaderboard(self) -> DataFrame:
        """Returns a dataframe representation of the current leaderboard, sorted by total score descending and with
        player names as row indexes and round numbers as columns """
        df = self.__leaderboard.copy(deep=True)
        df = df.dropna(how="all")
        df.loc["Total"] = df.sum()
        df = df.T.sort_values(by=["Total"], ascending=False).astype(int)
        return df

    def save(self, path: Path):
        df = self.full_leaderboard()
        df.to_csv(path)
