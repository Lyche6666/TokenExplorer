# test_tokenexplorer.py
"""
Tests for TokenExplorer module.
"""

import unittest
from tokenexplorer import TokenExplorer

class TestTokenExplorer(unittest.TestCase):
    """Test cases for TokenExplorer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenExplorer()
        self.assertIsInstance(instance, TokenExplorer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenExplorer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
