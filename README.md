# Reflective Agent

A Python implementation of a reflection pattern for AI responses using Google's Gemini models. This agent generates an initial response and then prompts the model to reflect on and improve its own output.

## Features

- **Reflection Pattern**: Implements a two-step process where the AI first responds, then reflects on and improves its response
- **Secure API Key Management**: Uses environment variables to keep sensitive API keys secure
- **Flexible Model Selection**: Supports different Gemini models
- **Error Handling**: Comprehensive error handling for configuration and API issues

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Get Your API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key

3. **Configure Environment**:
   Create a `.env` file in the project root:
   ```bash
   # .env
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

   **⚠️ Important**: Never commit your `.env` file to version control!

4. **Run the Agent**:
   ```bash
   python reflective_agent.py
   ```

## Usage

### Basic Usage
```python
from reflective_agent import reflect_and_improve

prompt = "Explain quantum computing in simple terms"
initial, improved = reflect_and_improve(prompt)

print("Initial:", initial)
print("Improved:", improved)
```

### Custom Model
```python
# Use a different Gemini model
initial, improved = reflect_and_improve(prompt, model="gemini-1.5-pro")
```

## How It Works

1. **Initial Response**: The model generates a response to your prompt
2. **Reflection**: The model reviews its own response and suggests improvements
3. **Output**: Returns both the original and improved versions

## Security Best Practices

- API keys are stored in environment variables, not in code
- The `.env` file is excluded from version control
- Clear error messages guide users to proper configuration
- No hardcoded sensitive information

## Requirements

- Python 3.7+
- Google AI API key
- Internet connection for API calls

## License

This project is open source and available under the MIT License.
