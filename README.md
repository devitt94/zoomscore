# zoomscore

A CLI application for keeping track of quiz leaderboards.

__Secondary Objectives__

> Your friends are using this quiz as the start of a quiz-championship over the coming
weeks and want you to keep track of the leaderboard. Suggest how you may store this
state reliably between quizzes and retrieve it on startup.
 
Currently the program will save the quiz results to a CSV file once the quiz has finished.
So keeping track of the previous quiz results would just be a matter of reading in the previous files and aggregating the scores.
If I had more time, I would improve this by instead loading the quiz results to some kind of SQL database.
That way we could have multiple different leagues of quizzes rather than just one, and store player/user information etc. so we could keep track of each person's performance across leagues/quizzes.

> You wish to distribute this as a tool such that other quiz groups can take advantage of the
system you’ve created, how would you package this and pass it onto others?

Assuming that many who will want to use the program may not be tech-savvy, the best way to do this would be to migrate it to a lightweight flask application with a simple web interface for creating/maintaining quizzes/leagues.

Alternatively, we could use setuptools to pacakge the program and list it on Pypi so that other Python programmers could make use of it or extend it.

> You want to make the leaderboard available such that participants in the championship
can see how they are doing as the weeks progress and during each quiz, how would you
achieve this?
 
As mentioned above, we could have our app update a database as the scores are entered
and a flask web app to display these results to the users.