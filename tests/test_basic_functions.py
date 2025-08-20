"""
Test basic functions of the Reflective Agent.
Tests the core reflect_and_improve functionality.
"""

import unittest
import sys
import os

# Add parent directory to path to import reflective_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reflective_agent import reflect_and_improve

class TestBasicFunctions(unittest.TestCase):
    """Test basic reflection functionality."""
    
    def setUp(self):
        """Set up test environment."""
        # Check if API key is available
        if not os.getenv('GOOGLE_API_KEY'):
            self.skipTest("GOOGLE_API_KEY not set in environment")
    
    def test_reflect_and_improve_basic(self):
        """Test basic reflect_and_improve function with simple prompt."""
        prompt = "What is 2+2?"
        
        try:
            initial, improved = reflect_and_improve(prompt)
            
            # Check that both responses are strings
            self.assertIsInstance(initial, str)
            self.assertIsInstance(improved, str)
            
            # Check that responses are not empty
            self.assertGreater(len(initial), 0)
            self.assertGreater(len(improved), 0)
            
            # Check that responses are different (improvement occurred)
            self.assertNotEqual(initial, improved)
            
            print(f"✓ Basic reflection test passed")
            print(f"  Initial response length: {len(initial)}")
            print(f"  Improved response length: {len(improved)}")
            
        except Exception as e:
            self.fail(f"Basic reflection test failed with error: {e}")
    
    def test_reflect_and_improve_complex(self):
        """Test reflect_and_improve with a more complex prompt."""
        prompt = "Explain the concept of recursion in programming with examples."
        
        try:
            initial, improved = reflect_and_improve(prompt)
            
            # Check response quality
            self.assertIsInstance(initial, str)
            self.assertIsInstance(improved, str)
            self.assertGreater(len(initial), 50)  # Should be substantial
            self.assertGreater(len(improved), 50)
            
            print(f"✓ Complex reflection test passed")
            print(f"  Initial response length: {len(initial)}")
            print(f"  Improved response length: {len(improved)}")
            
        except Exception as e:
            self.fail(f"Complex reflection test failed with error: {e}")
    
    def test_model_parameter(self):
        """Test that different models can be specified."""
        prompt = "What is artificial intelligence?"
        
        try:
            # Test with default model
            initial1, improved1 = reflect_and_improve(prompt)
            
            # Test with explicit model (should work the same)
            initial2, improved2 = reflect_and_improve(prompt, model="gemini-2.0-flash")
            
            # Responses should be similar (same model)
            self.assertIsInstance(initial1, str)
            self.assertIsInstance(initial2, str)
            
            print(f"✓ Model parameter test passed")
            
        except Exception as e:
            self.fail(f"Model parameter test failed with error: {e}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
