# test_stakecore.py
"""
Tests for StakeCore module.
"""

import unittest
from stakecore import StakeCore

class TestStakeCore(unittest.TestCase):
    """Test cases for StakeCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = StakeCore()
        self.assertIsInstance(instance, StakeCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = StakeCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
