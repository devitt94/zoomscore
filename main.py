from quiz import Quiz

# Menu options
DISPLAY_LEADERBOARD = 1
ENTER_SCORES = 2
QUIT = 3


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


def get_menu_option(round_num: int) -> int:
    """Displays the menu to the user and returns the selected menu option"""
    prompt = f"""
    Select from the menu options below
    {DISPLAY_LEADERBOARD}. Display leaderboard.
    {ENTER_SCORES}. Enter scores for round {round_num}
    {QUIT}. Exit the program.
    """
    s = input(prompt)
    try:
        opt = int(s)
        if opt not in (DISPLAY_LEADERBOARD, ENTER_SCORES, QUIT):
            raise ValueError
    except ValueError:
        print(f"Error: '{s}' is not a valid menu option")
        return get_menu_option(round_num)
    else:
        return opt


def main():
    quiz = initialise_quiz()
    while quiz.current_round is not None:
        _round = quiz.current_round
        opt = get_menu_option(_round)

        if opt == DISPLAY_LEADERBOARD:
            print(f"Leaderboard after round {_round - 1}:")
            print(quiz)
        elif opt == ENTER_SCORES:
            for player in quiz.players:
                update_player_score(quiz, player, _round)
        elif opt == QUIT:
            print("Exiting quiz.")

    print("Quiz is finished! Final leaderboard below:")
    print(quiz)


if __name__ == "__main__":
    main()
