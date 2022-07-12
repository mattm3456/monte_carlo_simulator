# Metadata:

### monte_carlo_simulator
### Matt Manner
### User ID: xkv3na
Monte Carlo Simulator for DS5100 Final Project

# Synopsis

## Installation:

To install the package, you must be in the repo.
To install, enter one of the following:

a) pip install . 
b) pip install -e . 
c) python setup.py install 
d) python setup.py develop

## Importing:

To import, you must include the following lines at the beginning of the file:

from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

These lines go into the montecarlo folder in the repo, then into the montecarlo.py file which has all of the methods, and grabs the methods. The methods are then usable in your notebook. 

Upon successful importing, you should receive a printed message: 'You have successfully installed the Monte Carlo modules'


## Creating Dice:

Example init: 
test_die = Die([1,2,3,4,5,6])
Then:
test_die.weightslist = [1, 1, 1, 1, 1, 1]
test_die.die = 
|   | face | weights |
|---|------|---------|
| 0 | 1    | 1       |
| 1 | 2    | 1       |
| 2 | 3    | 1       |
| 3 | 4    | 1       |
| 4 | 5    | 1       |
| 5 | 6    | 1       |

change_weight method:
test_die.change_weight(2,5)
Then: 
test_die.weightslist = [1, 5, 1, 1, 1, 1]

play_game method:
test_die.play_game(3)
Output:
[2, 5, 2]

display_dice method:
test_die.display_dice()
Output:
|   | face | weights |
|---|------|---------|
| 0 | 1    | 1       |
| 1 | 2    | 5       |
| 2 | 3    | 1       |
| 3 | 4    | 1       |
| 4 | 5    | 1       |
| 5 | 6    | 1       |

## Playing Games:


Example init: 
test_die1 = Die([1,2,3])
test_game = Game([test_die1, test_die2, test_die3])

play_the_game method:
test_game.play_the_game(3)

Output:
| Roll Number | Die 1 | Die 2 | Die 3 |
|-------------|-------|-------|-------|
| 1           | 2     | 1     | 3     |
| 2           | 3     | 2     | 3     |
| 3           | 2     | 2     | 2     |

show_df method with width "N":
test_game.show_df("N")

Output:

| Roll Number |       | Face Rolled |
|-------------|-------|-------------|
| 1           | Die 1 | 2           |
|             | Die 2 | 1           |
|             | Die 3 | 3           |
| 2           | Die 1 | 3           |
|             | Die 2 | 2           |
|             | Die 3 | 3           |
| 3           | Die 1 | 2           |
|             | Die 2 | 2           |
|             | Die 3 | 2           |

## Analyzing Games:

Example init:
test_analyzer = Analyzer(test_game)

jackpot method (testing the above game shown in Game.show_df()):
test_analyzer.jackpot()
| Roll Number | Die 1 | Die 2 | Die 3 |
|-------------|-------|-------|-------|
| 3           | 2     | 2     | 2     |

combos method:
test_analyzer.combos()

test_analyzer.permutations = 
| 0 | 1 | 2 | n |
|---|---|---|---|
| 1 | 2 | 3 | 1 |
| 2 | 3 | 3 | 1 |
| 2 | 2 | 2 | 1 |

counts_per_roll method:
test_analyzer.counts_per_roll()

Output:
| Roll Number | 1   | 2   | 3   |
|-------------|-----|-----|-----|
| 1           | 1.0 | 1.0 | 1.0 |
| 2           | 0.0 | 1.0 | 2.0 |
| 3           | 0.0 | 3.0 | 0.0 |


# API Description

## Die Class:

Die class takes in a list of numbers (floats or integers), strings, or a combination of both. There are four methods in this class, including the initializing method.

Initializing the die requires a list of faces, which can be numbers or strings.
        Example input: testing_die = Die([1, 2.5, 'cat'])
        Example outputs: 
        testing_die.faces = [1,2.5,'cat']
        testing_die.weightslist = [1,1,1]

change_weight requires a face input and a new weight for that face. The new weight must be a number, while the face can be either a string or a number (provided the face actually exists for the die). 
        Example input: testing_die.change_weight('cat',3)
        Example output: testing_die.weightslist = [1,1,3]
        

play_game returns a list of outcomes from a specified number of rolls for the Die object (default number of rolls is 1). The rolls use the object's weights to determine roll outcomes.
        Example input: testing_die.play_game(5)
        Example output: [2.5,'cat','cat',1,'cat']

display_dice returns the dataframe of die faces and corresponding weights.

## Game Class:

Game class takes in a list of dice. This class is used to actually play the game, and can return the results of the game in either a narrow or wide dataframe.

The initializer for the Game class requires input of a list of one or more Die objects.
        Example input: 
        die1 = Die([1,2,3])
        die2 = Die([4,5,6])
        die3 = Die([7,8,9])
        test_game = Game([die1, die2, die3])
        
        
play_the_game requires an input of n_plays, which is the number of desired rolls. Each die object instantiated will receive an equal number of rolls. 
        Example input: test_game.play_the_game(5)
        Example output: The output would be a DataFrame with "Roll Number" as the index (1-5), "Die 1", "Die 2", and "Die 3" as column names, with each value being the result of that specific roll of that specific die. 

show_df is used to display the results from the games, in a chosen format (narrow or wide).
        Example input: test_game.show_df('W') would show the game result in the default format (same as above) whereas test_game.show_df('N') would be a stacked version of the default, with a 2-column index, one column for roll number and one for die number.


## Analyzer Class:

Analyzer class is used to show game results in a different format, and also to show certain statistics about the game. It requires an instantiated Game object as input.

played_game would be an instantiated Game object from the previous class. In order to use most of the methods in the Analyzer class, the Game object must also be actually played (i.e. run the play_the_game method from the Game class).
        Example input: test_analyzer = Analyzer(test_game)
        
        
jackpot returns two outputs: a dataframe and an integer. The dataframe, self.jackpots_df, is the subset of the Game results dataframe where all the dice showed the same value (e.g. you rolled five 6's). The integer is the length of self.jackpots_df, which provides the total number of jackpots for your given game play.
        This method requires the display package from IPython.
        
        
combos returns the unique permutations present in your rolls, ordered by frequency. It considers order, meaning that if you roll 5 dice with a result of 1-2-3-4-5, that is considered different than 5-4-3-2-1. 
        The output of this will be a multi-index dataframe, with each Die as an index. The value for each die will appear in the index columns for each row, and the data column will be the number of occurences for that combination of die faces rolled. self.permutations will provide the number of combinations while taking order into consideration.
    
    
counts_per_roll gives another dataframe of the played game results. This one will have each face present in the die set as a column, the roll number as an index, and the number of times each face appears in the roll as the value.


# Manifest

Repo link: https://github.com/mattm3456/monte_carlo_simulator
Inside the repo, titled monte_carlo_simulator, the following files:

total 144
LICENSE
.gitignore
README.md
montecarlo_demo.ipynb
project_unit_testing_results.txt
setup.py
montecarlo
    __init__.py
    montecarlo.py
    montecarlo_tests.py