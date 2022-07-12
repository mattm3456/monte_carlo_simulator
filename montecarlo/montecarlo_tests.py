import unittest
import numpy as np
import pandas as pd
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer

class DieTestSuite(unittest.TestCase):
    def test_1_change_weight(self): 
        # Change a die's weights and confirm that it worked properly
        # add a book and test if it is in `book_list`.
        TestDie1 = Die([1,2,3,4,5,6])
        TestDie1.change_weight(3, 10)
        actual = TestDie1.weightslist
        expected = [1,1,10,1,1,1]
        self.assertEqual(actual, expected)
    
    def test_2_play_game(self):
        TestDie1 = Die([1,2,3,4,5,6])
        TestDie1.change_weight(2,0)
        TestDie1.change_weight(3,0)
        TestDie1.change_weight(4,0)
        TestDie1.change_weight(5,0)
        TestDie1.change_weight(6,0)
        TestDie1.play_game(5)
        actual = TestDie1.play_game(5)
        expected = [1,1,1,1,1]
        self.assertEqual(actual, expected)
        
        
    def test_3_display_dice(self):
        TestDie1 = Die([1,2,3,4,5,6])
        TestDie1.display_dice()
        actual = TestDie1.die
        expected = {'face':[1,2,3,4,5,6], 'weights': [1,1,1,1,1,1]}
###########################        
import unittest
class GameTestSuite(unittest.TestCase):
    def test_1_play_the_game_and_show(self): 
        # Play a game and check to see if you get a dataframe in return
        TestDie1 = Die([1])
        TestDie2 = Die([2])
        TestDie3 = Die([3])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        actual = TestGame.games_list.values.tolist()
        Testdf = pd.DataFrame({'Roll Number':[1,2,3,4,5], 'Die 1': [1,1,1,1,1], 'Die 2': [2,2,2,2,2], 'Die 3':[3,3,3,3,3]})
        Testdf = Testdf.set_index("Roll Number")
        expected = Testdf.values.tolist()
        self.assertEqual(actual, expected)
    
    def test_2_show_df_W(self):
        TestDie1 = Die([1])
        TestDie2 = Die([2])
        TestDie3 = Die([3])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        actual = TestGame.show_df("W").values.tolist()
        Testdf = pd.DataFrame({'Roll Number':[1,2,3,4,5], 'Die 1': [1,1,1,1,1], 'Die 2': [2,2,2,2,2], 'Die 3':[3,3,3,3,3]})
        Testdf = Testdf.set_index("Roll Number")
        expected = Testdf.values.tolist()
        self.assertEqual(actual, expected)
        
    def test_3_show_df_N(self):
        TestDie1 = Die([1])
        TestDie2 = Die([2])
        TestDie3 = Die([3])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        actual = TestGame.show_df("N").values.tolist()
        testlist = [[1],[2],[3]]
        expected = testlist * 5
        self.assertEqual(actual, expected)    

#####################
import unittest
class AnalyzerTestSuite(unittest.TestCase):
    def test_1_number_of_jackpots(self): 
        # Play a game and check to see if you get a dataframe in return
        TestDie1 = Die([1])
        TestDie2 = Die([1])
        TestDie3 = Die([1])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        TestAnalyzer = Analyzer(TestGame)
        TestAnalyzer.jackpot()
        actual = TestAnalyzer.number_of_jackpots
        expected = 5
        self.assertEqual(actual, expected)

    def test_2_combinations(self):
        TestDie1 = Die([1])
        TestDie2 = Die([1])
        TestDie3 = Die([1])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        TestAnalyzer = Analyzer(TestGame)
        TestAnalyzer.combos()
        actual = TestAnalyzer.combinations.values.tolist()
        expected = [[5]]
        self.assertEqual(actual, expected)
        
    def test_3_values_per_roll(self):
        TestDie1 = Die([1])
        TestDie2 = Die([1])
        TestDie3 = Die([1])
        TestGame = Game([TestDie1, TestDie2, TestDie3])
        TestGame.play_the_game(5)
        TestAnalyzer = Analyzer(TestGame)
        TestAnalyzer.counts_per_roll()
        actual = TestAnalyzer.counts_table.values.tolist()
        expected = pd.DataFrame({"Roll Number":[1,2,3,4,5], "1":[3,3,3,3,3]}).set_index("Roll Number").values.tolist()
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)