#!/usr/bin/python3
"""
Test file for user class
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """TestStateClass checks for the use of
    state class
    Args:
        unittest (): Propertys for unit testing
    """
    def test_create_istance(self):
        """create a new instance"""
        new_state = State()
        self.assertIsInstance(new_state, State)

    def test_create_istance2(self):
        """create a new instance"""
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)


if __name__ == '__main__':
    unittest.main()
