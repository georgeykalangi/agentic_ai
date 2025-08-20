"""
Test error handling and edge cases of the Reflective Agent.
Tests API key validation, network errors, and invalid inputs.
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add parent directory to path to import reflective_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reflective_agent import reflect_and_improve

class TestErrorHandling(unittest.TestCase):
    """Test error handling functionality."""
    
    def test_missing_api_key(self):
        """Test that missing API key raises appropriate error."""
        # Temporarily remove API key from environment
        original_key = os.environ.pop('GOOGLE_API_KEY', None)
        
        try:
            with self.assertRaises(ValueError) as context:
                reflect_and_improve("Test prompt")
            
            self.assertIn("GOOGLE_API_KEY environment variable not set", str(context.exception))
            print("✓ Missing API key test passed")
            
        finally:
            # Restore API key
            if original_key:
                os.environ['GOOGLE_API_KEY'] = original_key
    
    def test_empty_prompt(self):
        """Test handling of empty prompts."""
        if not os.getenv('GOOGLE_API_KEY'):
            self.skipTest("GOOGLE_API_KEY not set in environment")
        
        try:
            initial, improved = reflect_and_improve("")
            
            # Should handle empty prompt gracefully
            self.assertIsInstance(initial, str)
            self.assertIsInstance(improved, str)
            
            print("✓ Empty prompt test passed")
            
        except Exception as e:
            self.fail(f"Empty prompt test failed with error: {e}")
    
    def test_very_long_prompt(self):
        """Test handling of very long prompts."""
        if not os.getenv('GOOGLE_API_KEY'):
            self.skipTest("GOOGLE_API_KEY not set in environment")
        
        # Create a very long prompt
        long_prompt = "What is programming? " * 100
        
        try:
            initial, improved = reflect_and_improve(long_prompt)
            
            self.assertIsInstance(initial, str)
            self.assertIsInstance(improved, str)
            
            print("✓ Long prompt test passed")
            
        except Exception as e:
            self.fail(f"Long prompt test failed with error: {e}")
    
    def test_special_characters_prompt(self):
        """Test handling of prompts with special characters."""
        if not os.getenv('GOOGLE_API_KEY'):
            self.skipTest("GOOGLE_API_KEY not set in environment")
        
        special_prompt = "What does this mean: @#$%^&*()_+{}|:<>?[]\\;'\",./<>?"
        
        try:
            initial, improved = reflect_and_improve(special_prompt)
            
            self.assertIsInstance(initial, str)
            self.assertIsInstance(improved, str)
            
            print("✓ Special characters test passed")
            
        except Exception as e:
            self.fail(f"Special characters test failed with error: {e}")
    
    def test_unicode_prompt(self):
        """Test handling of unicode characters in prompts."""
        if not os.getenv('GOOGLE_API_KEY'):
            self.skipTest("GOOGLE_API_KEY not set in environment")
        
        unicode_prompt = "What is the meaning of: 🚀🌟💻🎯"
        
        try:
            initial, improved = reflect_and_improve(unicode_prompt)
            
            self.assertIsInstance(initial, str)
            self.assertIsInstance(improved, str)
            
            print("✓ Unicode characters test passed")
            
        except Exception as e:
            self.fail(f"Unicode characters test failed with error: {e}")

class TestMockResponses(unittest.TestCase):
    """Test with mocked API responses to avoid actual API calls."""
    
    @patch('reflective_agent.genai.Client')
    def test_mock_successful_response(self, mock_client):
        """Test with mocked successful API response."""
        # Mock the client and its methods
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        
        # Mock successful responses
        mock_instance.models.generate_content.side_effect = [
            MagicMock(text="Initial response"),
            MagicMock(text="Improved response")
        ]
        
        # Temporarily set a fake API key
        original_key = os.environ.get('GOOGLE_API_KEY')
        os.environ['GOOGLE_API_KEY'] = 'fake_key'
        
        try:
            initial, improved = reflect_and_improve("Test prompt")
            
            self.assertEqual(initial, "Initial response")
            self.assertEqual(improved, "Improved response")
            
            print("✓ Mock successful response test passed")
            
        finally:
            # Restore original API key
            if original_key:
                os.environ['GOOGLE_API_KEY'] = original_key
            else:
                os.environ.pop('GOOGLE_API_KEY', None)
    
    @patch('reflective_agent.genai.Client')
    def test_mock_api_error(self, mock_client):
        """Test handling of API errors."""
        # Mock the client to raise an exception
        mock_instance = MagicMock()
        mock_client.return_value = mock_instance
        mock_instance.models.generate_content.side_effect = Exception("API Error")
        
        # Temporarily set a fake API key
        original_key = os.environ.get('GOOGLE_API_KEY')
        os.environ['GOOGLE_API_KEY'] = 'fake_key'
        
        try:
            with self.assertRaises(Exception) as context:
                reflect_and_improve("Test prompt")
            
            self.assertIn("API Error", str(context.exception))
            print("✓ Mock API error test passed")
            
        finally:
            # Restore original API key
            if original_key:
                os.environ['GOOGLE_API_KEY'] = original_key
            else:
                os.environ.pop('GOOGLE_API_KEY', None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
