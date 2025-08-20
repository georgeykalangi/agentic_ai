"""
Test advanced functions of the Reflective Agent.
Tests multi-step reflection, response comparison, and batch processing.
"""

import unittest
import sys
import os

# Add parent directory to path to import reflective_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reflective_agent import (
    multi_step_reflection, 
    compare_responses, 
    batch_reflect
)

class TestAdvancedFunctions(unittest.TestCase):
    """Test advanced reflection functionality."""
    
    def setUp(self):
        """Set up test environment."""
        # Check if API key is available
        if not os.getenv('GOOGLE_API_KEY'):
            self.skipTest("GOOGLE_API_KEY not set in environment")
    
    def test_multi_step_reflection(self):
        """Test multi-step reflection with 2 steps."""
        prompt = "What is the difference between a list and a tuple in Python?"
        
        try:
            final_response = multi_step_reflection(prompt, steps=2)
            
            # Check that we get a string response
            self.assertIsInstance(final_response, str)
            self.assertGreater(len(final_response), 0)
            
            print(f"✓ Multi-step reflection test passed")
            print(f"  Final response length: {len(final_response)}")
            
        except Exception as e:
            self.fail(f"Multi-step reflection test failed with error: {e}")
    
    def test_multi_step_reflection_single_step(self):
        """Test multi-step reflection with 1 step (should work like basic reflection)."""
        prompt = "Explain what a function is in programming."
        
        try:
            final_response = multi_step_reflection(prompt, steps=1)
            
            self.assertIsInstance(final_response, str)
            self.assertGreater(len(final_response), 0)
            
            print(f"✓ Single-step reflection test passed")
            
        except Exception as e:
            self.fail(f"Single-step reflection test failed with error: {e}")
    
    def test_compare_responses(self):
        """Test response comparison functionality."""
        initial_response = "Python is a programming language."
        improved_response = "Python is a high-level, interpreted programming language known for its simplicity and readability."
        
        try:
            comparison, improved_comparison = compare_responses(initial_response, improved_response)
            
            # Check that we get comparison results
            self.assertIsInstance(comparison, str)
            self.assertIsInstance(improved_comparison, str)
            self.assertGreater(len(comparison), 0)
            self.assertGreater(len(improved_comparison), 0)
            
            print(f"✓ Response comparison test passed")
            print(f"  Comparison length: {len(comparison)}")
            
        except Exception as e:
            self.fail(f"Response comparison test failed with error: {e}")
    
    def test_batch_reflect(self):
        """Test batch processing of multiple prompts."""
        prompts = [
            "What is a variable?",
            "Explain loops in programming",
            "What is object-oriented programming?"
        ]
        
        try:
            results = batch_reflect(prompts)
            
            # Check that we get results for all prompts
            self.assertEqual(len(results), len(prompts))
            
            # Check structure of each result
            for result in results:
                self.assertIn('prompt', result)
                self.assertIn('initial', result)
                self.assertIn('improved', result)
                self.assertIsInstance(result['prompt'], str)
                self.assertIsInstance(result['initial'], str)
                self.assertIsInstance(result['improved'], str)
            
            print(f"✓ Batch reflection test passed")
            print(f"  Processed {len(results)} prompts successfully")
            
        except Exception as e:
            self.fail(f"Batch reflection test failed with error: {e}")
    
    def test_batch_reflect_single_prompt(self):
        """Test batch processing with a single prompt."""
        prompts = ["What is debugging?"]
        
        try:
            results = batch_reflect(prompts)
            
            self.assertEqual(len(results), 1)
            self.assertIn('prompt', results[0])
            self.assertIn('initial', results[0])
            self.assertIn('improved', results[0])
            
            print(f"✓ Single prompt batch test passed")
            
        except Exception as e:
            self.fail(f"Single prompt batch test failed with error: {e}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
