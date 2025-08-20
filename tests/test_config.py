"""
Test configuration and utilities for the Reflective Agent tests.
"""

import os
import sys
from typing import List, Dict, Any

# Test configuration
TEST_CONFIG = {
    'api_key_required': True,
    'max_test_duration': 300,  # 5 minutes max per test
    'retry_attempts': 3,
    'test_prompts': [
        "What is 2+2?",
        "Explain recursion",
        "What is machine learning?",
        "Describe the reflection pattern"
    ],
    'models_to_test': [
        "gemini-2.0-flash",
        # "gemini-1.5-pro"  # Uncomment to test other models
    ]
}

def get_test_prompts() -> List[str]:
    """Get list of test prompts."""
    return TEST_CONFIG['test_prompts']

def get_models_to_test() -> List[str]:
    """Get list of models to test."""
    return TEST_CONFIG['models_to_test']

def is_api_key_available() -> bool:
    """Check if API key is available for testing."""
    return bool(os.getenv('GOOGLE_API_KEY'))

def get_test_environment_info() -> Dict[str, Any]:
    """Get information about the test environment."""
    return {
        'python_version': sys.version,
        'api_key_available': is_api_key_available(),
        'working_directory': os.getcwd(),
        'test_directory': os.path.dirname(os.path.abspath(__file__)),
        'parent_directory': os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    }

def print_test_environment():
    """Print test environment information."""
    info = get_test_environment_info()
    print("🔧 Test Environment:")
    print(f"  Python Version: {info['python_version']}")
    print(f"  API Key Available: {'✅' if info['api_key_available'] else '❌'}")
    print(f"  Working Directory: {info['working_directory']}")
    print(f"  Test Directory: {info['test_directory']}")
    print(f"  Parent Directory: {info['parent_directory']}")
    print()

def create_test_prompt(category: str, complexity: str = "medium") -> str:
    """Create a test prompt based on category and complexity."""
    prompts = {
        'math': {
            'simple': "What is 5 + 3?",
            'medium': "Explain the concept of prime numbers",
            'complex': "Describe the relationship between calculus and physics"
        },
        'programming': {
            'simple': "What is a variable?",
            'medium': "Explain object-oriented programming",
            'complex': "Describe the design patterns used in microservices architecture"
        },
        'ai': {
            'simple': "What is artificial intelligence?",
            'medium': "Explain how neural networks work",
            'complex': "Describe the challenges of implementing AGI"
        }
    }
    
    return prompts.get(category, {}).get(complexity, "What is the meaning of life?")

def validate_test_result(result: Any, expected_type: type, min_length: int = 0) -> bool:
    """Validate a test result meets basic criteria."""
    if not isinstance(result, expected_type):
        return False
    
    if hasattr(result, '__len__') and len(result) < min_length:
        return False
    
    return True
