# Aji
Aji is a japanese term used in the game Go that roughly means 'latent potential.'  It refers to a played stone's ability to open various avenues of play. Aji is a Python implementation of the game Go with the intent to be a modular engine to hook into any interface that you want to play in--web app, mobile app, REST API, CLI, hardware project, etc.  The engine will run and interface via REST API.  Until support is ready, a barebones interactive CLI mode will be the only way to play.

Aji is a hobby project to use in my own educational playgrounds for whatever subfields of software design are catching my interest.

## Educational Goals
* Embrace Test Driven Development
* Explore Jira as a project management tool
* Gain experience building Docker Images
* Explore techniques to avoid feature creep

## To Install
Clone in the directory of your choice. Install pipenv:
> pip install pipenv

Navigate to the top level and run:
> pipenv install -r requirements.txt

[Article](https://docs.python-guide.org/dev/virtualenvs/) used for reference.

## To Run
> pipenv run src/aji/aji.py

## To Test
In top level directory, run:
> python -m unittest discover -s tests

## Go Rules
The rules of Go are simple.  Formalizing them is less so.  For the sake of implementation, Aji will use the *[Computer Olympiad](https://en.wikipedia.org/wiki/Computer_Olympiad)* Ruleset.  A soft goal is to to build to an interface that permits easily choosing between other rulesets and scoring methods.

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

# Long Cycle Rule
A board position is defined by the colouring of the grid’s intersections directly after play and any consequent removals.

If a play recreates a previous board position then exceptionally and immediately the game ends and is scored, based on an analysis of all moves played since the moment just after the first occurrence until the moment just after the last occurrence, as follows:

1. If between the two occurrences the difference in number of captured black and white stones is not zero, then the program that captured the most stones of the opposing colour wins the game.

2. If between the two occurrences the difference in number of captured black and white stones is zero, then the game ends as a draw. 

# Ending the game
1.  A game is played until both parties agree that it is finished.
2.  During  the  game,  if  one  player  resigns,  the  game is finished. 
3.  If both players pass one after the other, the game is finished.

## Living stones and dead stones
1. When the game is finished, by agreement of both parties, all un-removable stones are living stones.
2. When the game is finished, by agreement of both parties, all removable stones are dead stones.