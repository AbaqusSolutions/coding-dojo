from enum import Enum
import unittest

class Orientation(str, Enum):
    NORTH = "N"
    SOUTH = "S"
    WEST = "W"
    EAST = "E"
    
class Rotation(str, Enum):
    RIGHT = "R"
    LEFT = "L"

class MarsRover:

    def __init__(self, initial_orientation):
        self.orientation = initial_orientation

    def rotate(self, rotation):
        match self.orientation:
            case Orientation.NORTH:
                if rotation == Rotation.LEFT:
                    return Orientation.WEST
                
                elif rotation == Rotation.RIGHT:
                    return Orientation.EAST
            
            case Orientation.WEST:
                if rotation == Rotation.LEFT:
                    return Orientation.SOUTH
                
                elif rotation == Rotation.RIGHT:
                    return Orientation.NORTH
                
            case Orientation.EAST:
                if rotation == Rotation.LEFT:
                    return Orientation.NORTH
                
                elif rotation == Rotation.RIGHT:
                    return Orientation.SOUTH
            
            case Orientation.SOUTH:
                if rotation == Rotation.LEFT:
                    return Orientation.EAST
                
                elif rotation == Rotation.RIGHT:
                    return Orientation.WEST
        

class TestMarsRover(unittest.TestCase):
    
    def test_rotate_left_from_north(self):
        new_orientation = MarsRover(Orientation.NORTH).rotate(Rotation.LEFT)
        self.assertEqual(new_orientation, Orientation.WEST)
    
    def test_rotate_right_from_north(self):
        new_orientation = MarsRover(Orientation.NORTH).rotate(Rotation.RIGHT)
        self.assertEqual(new_orientation, Orientation.EAST)
    
    def test_rotate_left_from_west(self):
        new_orientation = MarsRover(Orientation.WEST).rotate(Rotation.LEFT)
        self.assertEqual(new_orientation, Orientation.SOUTH)

    def test_rotate_right_from_west(self):
        new_orientation = MarsRover(Orientation.WEST).rotate(Rotation.RIGHT)
        self.assertEqual(new_orientation, Orientation.NORTH)