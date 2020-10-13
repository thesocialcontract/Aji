# Aji
Aji is a japanese term used in the game Go that roughly means 'latent potential.'  It refers to a played stone's ability to open various avenues of play. Aji is a Python implementation of the game Go with the intent to be a modular engine to hook into any interface that you want to play in--web app, mobile app, REST API, CLI, hardware project, etc.  The engine will run and interface via REST API.  Until support is ready, a barebones interactive CLI mode will be the only way to play.  The engine is based off of the  the SGFMill library, and implements the Computer Olympiad Ruleset.

Aji is a hobby project to use in my own educational playgrounds for whatever subfields of software design are catching my interest.

## Exploratory Educational Goals
* Embrace Test Driven Development
* Explore Jira as a project management tool
* Gain experience building Docker Images
* Explore techniques to avoid feature creep

## Concrete Goals
* Play Go from the command line with hotseat multiplayer
* Play Go from the command line against an AI that makes random moves
* Play Go running from a Docker image
* Use unit tests to verify functional correctness whenver possible (rather than running the entire program.)
* Split development effort into Jira cards.  No work is done without a Jira.

## Purpose of Goals
* Specific goals to make a functional program help keep me on target.
* Test Driven Development is difficult, and not often practiced without a mandate from on high or a team that already buys into it.  In my anecdotal experience and the experience of otehrs, Universities don't really teach you what makes a good test or TDD.  "Tests are good and you should write them."  But how?  Why?  When?  Writing tests take effort, and they're easy to screw up.  Without an external force pushing you to write tests, developers take the path of least resistance and often won't.  I want to understand what makes TDD worth the effort. What makes it difficult? What sorts of mistakes do you often make in TDD? How do you resolve those?  How TDD shapes your design?  What benefits do you get from TDD, and what drawbacks are there?  Is TDD worth the effort or is it industry hype?
* Jira cards are *way* more cumbersome than this project needs.  However, speed is not the purpose of this project, education is.  Making jiras myself accomplishes two things. (1) They force me to be deliberate.  Jiras split the project into discrete goals and keeps me from getting distracted by shiny new features or fixes that aren't relevant to my overall goal, and (2) screwing up cards (descriptions, scope, etc.) will inform me of what sorts of Jiras are actually helpful for a developer.

## To Install
Clone in the directory of your choice. Install pipenv:
`pip install pipenv`

Optional: Activate a virtual environment to isolate dependencies from your system.  Navigate to the top level and run:
`pipenv shell`

Navigate to the top level and run:
`pipenv install -r requirements.txt`

[Article](https://docs.python-guide.org/dev/virtualenvs/) used for reference.

## To Run
`pipenv run src/aji/aji.py`

## To Test
In top level directory, run 
`python -m unittest discover -s tests`

## Go Rules
The rules of Go are simple.  Formalizing them is less so.  For the sake of implementation, Aji will use the *[Computer Olympiad](https://en.wikipedia.org/wiki/Computer_Olympiad)* Ruleset.  A soft goal is to build to an interface that permits easily choosing between other rulesets and scoring methods.

### Chinese Rules
- Scoring: Area
- Counting Method:

Specific features:
    Only the points of one player are counted to determine the result. 

## ComputerOlympiadRules

> * **Scoring method:** Area
> * **Counting method:** Chinese
> * **Repetition:** Superko (but sometimes alternative procedures are followed when a position repeats)
> * **Komi:** 7.5
> * **Suicide:** Forbidden
> * **Points in seki:** Count
> * **Cost of moving in one's territory:** 0 points; cost of moving in opponent's territory: 0 points; benefit of moving in unclaimed territory: 1 point.
> * **Life and death settled by:** Game resumption
> * **Illegal move:** Is regarded as a pass 

## Long Cycle Rule
A board position is defined by the colouring of the grid’s intersections directly after play and any consequent removals.

If a play recreates a previous board position then exceptionally and immediately the game ends and is scored, based on an analysis of all moves played since the moment just after the first occurrence until the moment just after the last occurrence, as follows:

1. If between the two occurrences the difference in number of captured black and white stones is not zero, then the program that captured the most stones of the opposing colour wins the game.

2. If between the two occurrences the difference in number of captured black and white stones is zero, then the game ends as a draw. 

## Ending the game
1.  A game is played until both parties agree that it is finished.
2.  During  the  game,  if  one  player  resigns,  the  game is finished. 
3.  If both players pass one after the other, the game is finished.

## Living stones and dead stones
1. When the game is finished, by agreement of both parties, all un-removable stones are living stones.
2. When the game is finished, by agreement of both parties, all removable stones are dead stones.

# Libraries Used
[SGFMill](https://mjw.woodcraft.me.uk/sgfmill/doc/1.1.1/intro.html)