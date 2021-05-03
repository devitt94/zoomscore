from quiz import Quiz


def update_player_score(quiz: Quiz, player: str, round_num: int) -> None:
    """Updates the leaderboard with the score for a given player and round_number."""
    s = input(f"Enter {player}'s score for round {round_num}: ")
    try:
        score = int(s)
        quiz.add_score(player, score)
    except ValueError:
        print(f"Error adding score '{s}' for {player}. Please try again")
        update_player_score(quiz, player, round_num)


def initialise_quiz() -> Quiz:
    """Retrieves quiz parameters from the user and returns a Quiz object based on those parameters."""
    try:
        num_players = int(input("Enter number of players: "))
        players = []
        for i in range(num_players):
            player_name = input(f"Enter player {i+1} name: ")
            players.append(player_name)

        num_rounds = int(input("Enter number of rounds: "))
        round_length = int(input("Enter number of questions in each round: "))
        quiz = Quiz(players, num_rounds, round_length)
    except Exception:
        print("Got an error trying to initialise the quiz. Please try again.")
        return initialise_quiz()
    else:
        return quiz


def main():
    quiz = initialise_quiz()
    while quiz.current_round is not None:
        _round = quiz.current_round
        for player in quiz.players:
            update_player_score(quiz, player, _round)

        print(f"Scores after round {_round} below:")
        print(quiz)

    print("Quiz is finished! Final leaderboard below:")
    print(quiz)


if __name__ == "__main__":
    main()