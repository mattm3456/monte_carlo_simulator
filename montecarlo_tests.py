import unittest
import numpy as np
import pandas as pd
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

class DieTestSuite(unittest.TestCase):
    def test_1_change_weight(self): 
         '''
        tests whether the change_weight function works. Changes weight #3 in a test die to 10. Confirms that resulting weights_list is [1,1,10,1,1,1]
        '''
        TestDie1 = Die([1,2,3,4,5,6])
        TestDie1.change_weight(3, 10)
        actual = TestDie1.weightslist
        expected = [1,1,10,1,1,1]
        message = "Test failed: weight change didn't work properly !"
        self.assertEqual(actual, expected, message)
    
    def test_2_play_game(self):
        '''
        Tests the play_game method by setting all weights except face #1 to 0. This means that all rolls will result in a value of 1. Playing the game 5 times should result in a games outcome list of [1,1,1,1,1].
        '''
        TestDie1 = Die([1,2,3,4,5,6])
        TestDie1.change_weight(2,0)
        TestDie1.change_weight(3,0)
        TestDie1.change_weight(4,0)
        TestDie1.change_weight(5,0)
        TestDie1.change_weight(6,0)
        TestDie1.play_game(5)
        actual = TestDie1.play_game(5)
        expected = [1,1,1,1,1]
        message = "Gameplay didn't work properly !"
        self.assertEqual(actual, expected, message)
        
        
    def test_3_display_dice(self):
        '''
        Tests the display_dice method, to confirm that die dictionary is made as expected.
        '''
        TestDie1 = Die([1,2,3,4,5,6])
        TestDie1.display_dice()
        actual = TestDie1.die
        expected = {'face':[1,2,3,4,5,6], 'weights': [1,1,1,1,1,1]}
        message = "Die dictionary not made properly!"
        self.assertEqual(actual, expected, message)
        
###########################        
class GameTestSuite(unittest.TestCase):
    def test_1_play_the_game_and_show(self): 
        '''
        Plays a game and confirms that output is in proper format. Converts the outcome dataframe to a list and compares against a hard-coded analogous list.
        '''
        TestDie1 = Die([1])
        TestDie2 = Die([2])
        TestDie3 = Die([3])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        actual = TestGame.games_list.values.tolist()
        Testdf = pd.DataFrame({'Roll Number':[1,2,3,4,5], 'Die 1': [1,1,1,1,1], 'Die 2': [2,2,2,2,2], 'Die 3':[3,3,3,3,3]})
        Testdf = Testdf.set_index("Roll Number")
        expected = Testdf.values.tolist()
        message = "Gameplay method not working properly !"
        self.assertEqual(actual, expected, message)
    
    def test_2_show_df_W(self):
        '''
        Shows a dataframe converted to list format as in previous test.
        '''
        TestDie1 = Die([1])
        TestDie2 = Die([2])
        TestDie3 = Die([3])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        actual = TestGame.show_df("W").values.tolist()
        Testdf = pd.DataFrame({'Roll Number':[1,2,3,4,5], 'Die 1': [1,1,1,1,1], 'Die 2': [2,2,2,2,2], 'Die 3':[3,3,3,3,3]})
        Testdf = Testdf.set_index("Roll Number")
        expected = Testdf.values.tolist()
        message = "Gameplay dataframe creation error"
        self.assertEqual(actual, expected, message)
        
    def test_3_show_df_N(self):
        '''
        Similar to test_3_show_df_W, but uses a narrow DataFrame to make the list.
        '''
        TestDie1 = Die([1])
        TestDie2 = Die([2])
        TestDie3 = Die([3])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        actual = TestGame.show_df("N").values.tolist()
        testlist = [[1],[2],[3]]
        expected = testlist * 5
        message = "Converting to narrow dataframe error!"
        self.assertEqual(actual, expected, message)    

#####################
class AnalyzerTestSuite(unittest.TestCase):
    def test_1_number_of_jackpots(self): 
        '''
        Initializes a Game and Analyzer with 3 Die with only 1 face each. Should roll a Jackpot every roll, so this test confirms that.
        '''
        TestDie1 = Die([1])
        TestDie2 = Die([1])
        TestDie3 = Die([1])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        TestAnalyzer = Analyzer(TestGame)
        TestAnalyzer.jackpot()
        actual = TestAnalyzer.number_of_jackpots
        expected = 5
        message = "Jackpots not properly running"
        self.assertEqual(actual, expected, message)

    def test_2_combinations(self):
        '''
        This test confirms that every roll of 3 equivalent single-faced dice returns the same combination. The expected outcome of the TestAnalyzer is a dataframe of 1 combination, 5 times.
        '''
        TestDie1 = Die([1])
        TestDie2 = Die([1])
        TestDie3 = Die([1])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        TestAnalyzer = Analyzer(TestGame)
        TestAnalyzer.combos()
        actual = TestAnalyzer.combinations.values.tolist()
        expected = [[5]]
        message = "Not properly calculating combinations!"
        self.assertEqual(actual, expected, message)
        
    def test_3_values_per_roll(self):
        '''
        test_3_values_per_roll confirms the counts_per_roll method in the Analyzer class. Checks that there is one column for the one existing face (1), and that all 3 dice rolled 1 for each roll.
        '''
        TestDie1 = Die([1])
        TestDie2 = Die([1])
        TestDie3 = Die([1])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        TestAnalyzer = Analyzer(TestGame)
        TestAnalyzer.counts_per_roll()
        actual = TestAnalyzer.counts_table.values.tolist()
        expected = pd.DataFrame({"Roll Number":[1,2,3,4,5], "1":[3,3,3,3,3]}).set_index("Roll Number").values.tolist()
        message = "Not properly calculating values for each roll !"
        self.assertEqual(actual, expected, message)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)