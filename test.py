import unittest

from quiz import Quiz


class QuizTest(unittest.TestCase):

    def setUp(self) -> None:
        players = [f"Player{i}" for i in range(1, 5)]
        self.quiz = Quiz(players, num_rounds=2, round_length=5)

    def test_init(self):
        with self.assertRaises(AssertionError):
            Quiz(["Player1"])

        players = ["Player1", "Player2"]
        quiz = Quiz(players)
        self.assertEqual(quiz.players, players)
        self.assertEqual(quiz.current_round, 1)

    def test_add_score(self):
        with self.assertRaises(KeyError):
            self.quiz.add_score("UnknownPlayer", 1)

        with self.assertRaises(ValueError):
            self.quiz.add_score("Player1", -1)

        with self.assertRaises(ValueError):
            self.quiz.add_score("Player2", 6)

        self.quiz.add_score("Player1", 5)
        self.quiz.add_score("Player2", 3)
        self.quiz.add_score("Player3", 4)
        self.quiz.add_score("Player4", 2)
        self.assertEqual(self.quiz.current_round, 2)
        self.quiz.add_score("Player1", 4)
        self.quiz.add_score("Player2", 2)
        self.quiz.add_score("Player3", 3)
        self.quiz.add_score("Player4", 1)
        self.assertIsNone(self.quiz.current_round)

        with self.assertRaises(RuntimeError):
            self.quiz.add_score("Player1", 4)

    def tearDown(self) -> None:
        del self.quiz


if __name__ == '__main__':
    unittest.main()
