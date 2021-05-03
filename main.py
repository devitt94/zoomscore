from quiz import Quiz


def update_player_score(quiz: Quiz, player: str, round_num: int) -> None:
    pass


def initialise_quiz() -> Quiz:
    pass


if __name__ == "__main__":
    quiz = initialise_quiz()
    while quiz.current_round is not None:
        _round = quiz.current_round
        for player in quiz.players:
            update_player_score(quiz, player, _round)

        print(f"Scores after round {_round} below:")
        print(quiz)

    print("Quiz is finished! Final leaderboard below:")
    print(quiz)
