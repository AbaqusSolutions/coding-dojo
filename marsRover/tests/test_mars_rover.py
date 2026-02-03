import unittest
from mars_rover import sum_numbers, next_state

class TestMarsRover(unittest.TestCase):
    
    def test_north_turn_left(self):
        self.assertEqual( next_state((1, 2, 'N'), 'L'  ), (1, 2, 'W') )

    def test_west_turn_left(self):
        self.assertEqual( next_state((1, 2, 'W'), 'L'  ), (1, 2, 'S') )

    def test_south_turn_left(self):
        self.assertEqual( next_state((1, 2, 'S'), 'L'  ), (1, 2, 'E') )

    def test_east_turn_left(self):
        self.assertEqual( next_state((1, 2, 'E'), 'L'  ), (1, 2, 'N') )
        
    def test_north_turn_right(self):
        self.assertEqual( next_state((1, 2, 'N'), 'R'  ), (1, 2, 'E') )

    def test_west_turn_right(self):
        self.assertEqual( next_state((1, 2, 'W'), 'R'  ), (1, 2, 'N') )

    def test_south_turn_right(self):
        self.assertEqual( next_state((1, 2, 'S'), 'R'  ), (1, 2, 'W') )

    def test_east_turn_right(self):
        self.assertEqual( next_state((1, 2, 'E'), 'R'  ), (1, 2, 'S') )

    ## mov test
    def test_move_north(self):
        self.assertEqual( next_state((1, 2, 'N'), 'M' ) , (1, 3, 'N') )

    def test_margin_north(self):
        self.assertEqual(

        )