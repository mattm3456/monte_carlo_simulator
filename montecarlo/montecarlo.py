import numpy as np
import pandas as pd
class Die():
    '''
    Die class takes in a list of numbers (floats or integers), strings, or a combination of both. There are four methods in this class, including the initializing method
    '''
    
    def __init__(self, faces):
        
        '''
        Initializing the die requires a list of faces, which can be numbers or strings.
        Example input: testing_die = Die([1, 2.5, 'cat'])
        Example outputs: 
        testing_die.faces = [1,2.5,'cat']
        testing_die.weightslist = [1,1,1]
        '''
        
        for i in faces:
            if type(i) != float and type(i) != int and type(i) != str:
                print("Die must be a list of numbers or strings")
                
        self.faces = faces
        self.weightslist = [1] * len(faces)
        self.die = pd.DataFrame({'face': self.faces,'weights': self.weightslist})
    
    def change_weight(self, j, new_weight):
        '''
        change_weight requires a face input and a new weight for that face. The new weight must be a number, while the face can be either a string or a number (provided the face actually exists for the die). 
        Example input: testing_die.change_weight('cat',3)
        Example output: testing_die.weightslist = [1,1,3]
        '''
        
        if type(new_weight) != float and type(new_weight) != int:
            print('This is not a valid weight')
        elif type(new_weight) == float or type(new_weight) == int:
            if j in self.faces:
                index_finder = self.faces.index(j)
                self.weightslist[index_finder] = new_weight
            elif j not in self.faces:
                print("This face is not in the die")
        
        self.die = pd.DataFrame({'face': self.faces,'weights': self.weightslist})
        
    def play_game(self, number_rolls = 1):
        '''
        play_game returns a list of outcomes from a specified number of rolls for the Die object (default number of rolls is 1). The rolls use the object's weights to determine roll outcomes.
        Example input: testing_die.play_game(5)
        Example output: [2.5,'cat','cat',1,'cat']
        '''
        
        game_results = [self.die.face.sample(weights=self.weightslist).values[0] for i in range(number_rolls)]
        return(game_results)
        
    def display_dice(self):
        
        '''
        display_dice returns the dataframe of die faces and corresponding weights.
        '''
        print(self.die)
        
#############

class Game():
    '''
    Game class takes in a list of dice. This class is used to actually play the game, and can return the results of the game in either a narrow or wide dataframe.
    '''
    
    def __init__(self, dice):
        '''
        The initializer for the Game class requires input of a list of one or more Die objects.
        Example input: 
        die1 = Die([1,2,3])
        die2 = Die([4,5,6])
        die3 = Die([7,8,9])
        test_game = Game([die1, die2, die3])
        '''
        self.dice = dice
        
    def play_the_game(self, n_plays):
        '''
        play_the_game requires an input of n_plays, which is the number of desired rolls. Each die object instantiated will receive an equal number of rolls. 
        Example input: test_game.play_the_game(5)
        Example output: __games_list would be a DataFrame with "Roll Number" as the index (1-5), "Die 1", "Die 2", and "Die 3" as column names, with each value being the result of that specific roll of that specific die. 
        '''
        self.n_plays = n_plays
        dice_count = 1
        global dice_names 
        dice_names = []
        global numb_roll 
        numb_roll = []
        global dices 
        dices = {}
        global __games_list 
        __games_list = pd.DataFrame(dices)

        for i in self.dice:
            die_name = 'Die' + str(dice_count)
            dice_names.append(die_name)
            dices[die_name] = []
            dice_count += 1    
   
        c = 0

        for dice_piece in self.dice:
            c += 1
            col = []
            for play in range(self.n_plays):
                die_name = 'Die ' + str(c)
                roll = dice_piece.play_game()
                if c == 1:
                    numb_roll.append(play + 1)
                col.append(roll)

            __games_list[die_name] = col
            __games_list[die_name] = __games_list[die_name].str[0]
        __games_list['Roll Number'] = numb_roll
                
        __games_list.set_index("Roll Number", inplace = True)
        self.games_list = __games_list
        return __games_list
        
    def show_df(self, width = 'W'):
        '''show_df is used to display the results from the games, in a chosen format (narrow or wide).
        
        Example input: test_game.show_df('W') would show the game result in the default format (same as above) whereas test_game.show_df('N') would be a stacked version of the default, with a 2-column index, one column for roll number and one for die number.
        '''
        
        if width == "N" or width == "W" or width == "":
            dummy_variable = 1
        try:
            dummy_variable 
        except: 
            print('Width must be set to either N (for narrow) or W (for wide). Default is set to wide')

        if width == "W" or width == "":
            return __games_list
        elif width == "N":
            games_narrow = __games_list.stack().to_frame('Face Rolled')
            return games_narrow
            
#############

from collections import Counter
from IPython.display import display

class Analyzer():
    '''
    Analyzer class is used to show game results in a different format, and also to show certain statistics about the game. It requires an instantiated Game object as input.
    '''
    
    def __init__(self, played_game):
        '''
        played_game would be an instantiated Game object from the previous class. In order to use most of the methods in the Analyzer class, the Game object must also be actually played (i.e. run the play_the_game method from the Game class).
        Example input: test_analyzer = Analyzer(test_game)
        '''
        
        self.played_game = played_game
        global Play 
        Play = self.played_game.show_df()
    
    def jackpot(self):
        '''
        jackpot returns two outputs: a dataframe and an integer. The dataframe, self.jackpots_df, is the subset of the Game results dataframe where all the dice showed the same value (e.g. you rolled five 6's). The integer is the length of self.jackpots_df, which provides the total number of jackpots for your given game play.
        This method requires the display package from IPython.
        '''
        
        Jackpots = Play.eq(Play.iloc[:, 0], axis=0).all(1)
        Jackpots = Jackpots[Jackpots]
        JackPots_DF = display(Play.loc[Jackpots.index])
        self.jackpots_df = JackPots_DF
        self.number_of_jackpots = len(Jackpots)
        print(self.number_of_jackpots)
        return self.jackpots_df
        
    def combos(self):
        '''
        combos returns the unique permutations present in your rolls, ordered by frequency. It considers order, meaning that if you roll 5 dice with a result of 1-2-3-4-5, that is considered different than 5-4-3-2-1. 
        The output of this will be a multi-index dataframe, with each Die as an index. The value for each die will appear in the index columns for each row, and the data column will be the number of occurences for that permutation of die faces rolled.
        '''
        
        combos_rolls2 = pd.DataFrame(Play.value_counts())
        combos_rolls2.columns =['Number of Occurences']
        combos_rolls2.apply(Counter, axis='columns').value_counts()
        combonations = Play.apply(lambda x: pd.Series(sorted(x)), 1)\
 .value_counts()\
 .to_frame('n')
        self.combonations = combonations
        self.combinations = combos_rolls2

    def counts_per_roll(self):
        '''
        counts_per_roll gives another dataframe of the played game results. This one will have each face present in the die set as a column, the roll number as an index, and the number of times each face appears in the roll as the value.
        '''
        
        self.counts_table = Play.apply(pd.Series.value_counts, axis=1).fillna(0)
        return self.counts_table
        