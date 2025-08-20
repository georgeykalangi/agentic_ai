# Testing Guide for Reflective Agent

This folder contains comprehensive tests for the Reflective Agent implementation.

## 🧪 Test Structure

```
tests/
├── __init__.py              # Makes tests a Python package
├── test_basic_functions.py  # Tests core reflection functionality
├── test_advanced_functions.py # Tests multi-step, comparison, batch features
├── test_error_handling.py   # Tests error cases and edge conditions
├── test_config.py           # Test configuration and utilities
├── run_all_tests.py         # Main test runner script
└── README.md                # This file
```

## 🚀 Running Tests

### Run All Tests
```bash
# From the project root directory
python tests/run_all_tests.py

# Or from the tests directory
cd tests
python run_all_tests.py
```

### Run Specific Test Files
```bash
# Run only basic function tests
python tests/run_all_tests.py test_basic_functions

# Run only advanced function tests
python tests/run_all_tests.py test_advanced_functions

# Run only error handling tests
python tests/run_all_tests.py test_error_handling
```

### Run Individual Test Files
```bash
# Run basic tests directly
python tests/test_basic_functions.py

# Run advanced tests directly
python tests/test_advanced_functions.py

# Run error handling tests directly
python tests/test_error_handling.py
```

### Run with Python's unittest module
```bash
# Discover and run all tests
python -m unittest discover tests

# Run specific test class
python -m unittest tests.test_basic_functions.TestBasicFunctions

# Run specific test method
python -m unittest tests.test_basic_functions.TestBasicFunctions.test_reflect_and_improve_basic
```

## 📋 Test Categories

### 1. **Basic Functions** (`test_basic_functions.py`)
- ✅ Core `reflect_and_improve()` functionality
- ✅ Simple and complex prompt handling
- ✅ Model parameter validation
- ✅ Response quality verification

### 2. **Advanced Functions** (`test_advanced_functions.py`)
- ✅ Multi-step reflection cycles
- ✅ Response comparison analysis
- ✅ Batch processing of multiple prompts
- ✅ Edge cases for advanced features

### 3. **Error Handling** (`test_error_handling.py`)
- ✅ Missing API key validation
- ✅ Empty and invalid prompt handling
- ✅ Special characters and unicode support
- ✅ Mock API responses for offline testing

## ⚙️ Test Configuration

The `test_config.py` file contains:
- Test prompts and models to test
- Environment validation utilities
- Helper functions for creating test data
- Result validation utilities

## 🔑 Prerequisites

### Required Environment Variables
```bash
# Set your Google API key
export GOOGLE_API_KEY="your_api_key_here"

# Or create a .env file in the project root
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

### Required Dependencies
```bash
pip install -r requirements.txt
```

## 📊 Test Output

### Successful Test Run
```
🧪 Reflective Agent Test Suite
==================================================
Started at: 2024-01-15 10:30:00

test_reflect_and_improve_basic (__main__.TestBasicFunctions) ... ✓ Basic reflection test passed
  Initial response length: 45
  Improved response length: 67
ok
test_reflect_and_improve_complex (__main__.TestBasicFunctions) ... ✓ Complex reflection test passed
  Initial response length: 234
  Improved response length: 456
ok

==================================================
📊 Test Summary
==================================================
Tests run: 2
Failures: 0
Errors: 0
Skipped: 0

🎉 All tests passed successfully!
```

### Failed Test Run
```
❌ Failures:
  - test_reflect_and_improve_basic: API key not found
  - test_model_parameter: Network timeout

💥 Errors:
  - test_batch_reflect: Connection refused
```

## 🛠️ Writing New Tests

### Test File Template
```python
"""
Test description for the new functionality.
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reflective_agent import your_function_name

class TestYourFunction(unittest.TestCase):
    """Test your new functionality."""
    
    def setUp(self):
        """Set up test environment."""
        if not os.getenv('GOOGLE_API_KEY'):
            self.skipTest("GOOGLE_API_KEY not set in environment")
    
    def test_your_function_basic(self):
        """Test basic functionality."""
        # Your test code here
        result = your_function_name("test input")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        print("✓ Your test passed")

if __name__ == '__main__':
    unittest.main(verbosity=2)
```

### Test Naming Conventions
- Test methods: `test_functionality_description`
- Test classes: `TestFunctionality`
- Test files: `test_functionality.py`

### Best Practices
1. **Use descriptive names** for test methods
2. **Test one thing at a time** per test method
3. **Include setup and teardown** when needed
4. **Handle API key availability** gracefully
5. **Use meaningful assertions** with clear error messages
6. **Add print statements** for successful tests to track progress

## 🔍 Debugging Tests

### Verbose Output
```bash
python -m unittest tests.test_basic_functions -v
```

### Single Test Debugging
```bash
# Run single test with full output
python -m unittest tests.test_basic_functions.TestBasicFunctions.test_reflect_and_improve_basic -v
```

### Environment Check
```python
from tests.test_config import print_test_environment
print_test_environment()
```

## 📈 Continuous Integration

### GitHub Actions Example
```yaml
name: Test Reflective Agent
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python tests/run_all_tests.py
        env:
          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
```

## 🚨 Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure you're running from the project root
   - Check that `sys.path.append()` is working correctly

2. **API Key Issues**
   - Verify `.env` file exists and contains `GOOGLE_API_KEY`
   - Check environment variable is set: `echo $GOOGLE_API_KEY`

3. **Network Errors**
   - Check internet connection
   - Verify Google AI API is accessible
   - Check API rate limits

4. **Test Discovery Issues**
   - Ensure all test files start with `test_`
   - Check that test classes inherit from `unittest.TestCase`
   - Verify test methods start with `test_`

### Getting Help
- Check the test output for specific error messages
- Review the test configuration in `test_config.py`
- Ensure all dependencies are installed
- Verify your API key is valid and has sufficient quota
