import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def reflect_and_improve(prompt, model="gemini-2.0-flash"):
    """
    Implements a reflection pattern for AI responses.
    
    Args:
        prompt (str): The initial prompt for the model
        model (str): The model to use, defaults to "gemini-2.0-flash"
    
    Returns:
        tuple: (initial_text, improved_text) - both the original and improved responses
    """
    # Get API key from environment variable for security
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. Please create a .env file with your API key.")
    
    # Initialize client with API key from environment
    client = genai.Client(api_key=api_key)
    
    # Generate initial response
    initial_response = client.models.generate_content(
        model=model,
        contents=prompt
    )
    initial_text = initial_response.text
    
    # Prompt the model to reflect on its response
    reflection_prompt = f"Review the following response and suggest improvements:\n\n{initial_text}"
    reflection_response = client.models.generate_content(
        model=model,
        contents=reflection_prompt
    )
    improved_text = reflection_response.text
    
    return initial_text, improved_text

def multi_step_reflection(prompt, steps=3, model="gemini-2.0-flash"):
    """
    Perform multiple reflection cycles for deeper improvement.
    
    Args:
        prompt (str): The initial prompt for the model
        steps (int): Number of reflection cycles to perform
        model (str): The model to use
    
    Returns:
        str: The final improved response after multiple reflection cycles
    """
    current_response = prompt
    for i in range(steps):
        print(f"Reflection step {i+1}/{steps}...")
        current_response, improved = reflect_and_improve(current_response, model)
        current_response = improved
    return current_response

def compare_responses(initial, improved, model="gemini-2.0-flash"):
    """
    Analyze the differences between initial and improved responses.
    
    Args:
        initial (str): The initial response
        improved (str): The improved response
        model (str): The model to use for comparison
    
    Returns:
        tuple: (comparison_text, improved_comparison) - analysis and further improvements
    """
    comparison_prompt = f"""
    Compare these two responses and highlight:
    1. What was improved
    2. What remained the same
    3. Specific changes made
    
    Initial: {initial}
    Improved: {improved}
    """
    return reflect_and_improve(comparison_prompt, model)

def batch_reflect(prompts, model="gemini-2.0-flash"):
    """
    Process multiple prompts with reflection.
    
    Args:
        prompts (list): List of prompts to process
        model (str): The model to use
    
    Returns:
        list: List of dictionaries containing results for each prompt
    """
    results = []
    for i, prompt in enumerate(prompts):
        print(f"Processing prompt {i+1}/{len(prompts)}: {prompt[:50]}...")
        initial, improved = reflect_and_improve(prompt, model)
        results.append({
            "prompt": prompt,
            "initial": initial,
            "improved": improved
        })
    return results

def main():
    """Example usage of the reflective agent."""
    print("=== Reflective Agent Demo ===\n")
    
    # Example 1: Basic reflection
    print("1. Basic Reflection:")
    prompt = "Explain the significance of the Reflection Pattern in AI development."
    
    try:
        initial, improved = reflect_and_improve(prompt)
        
        print("=== Initial Response ===")
        print(initial[:200] + "..." if len(initial) > 200 else initial)
        print("\n=== Improved Response ===")
        print(improved[:200] + "..." if len(improved) > 200 else improved)
        
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("Please create a .env file with your GOOGLE_API_KEY")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Multi-step reflection
    print("\n" + "="*50)
    print("2. Multi-Step Reflection (2 steps):")
    try:
        multi_improved = multi_step_reflection("What is machine learning?", steps=2)
        print("\n=== Final Improved Response ===")
        print(multi_improved[:300] + "..." if len(multi_improved) > 300 else multi_improved)
    except Exception as e:
        print(f"Error in multi-step reflection: {e}")
    
    # Example 3: Response comparison
    print("\n" + "="*50)
    print("3. Response Comparison:")
    try:
        comparison, improved_comparison = compare_responses(
            "AI is a technology that helps computers think.",
            "Artificial Intelligence (AI) is a branch of computer science that enables machines to perform tasks that typically require human intelligence, including learning, reasoning, and problem-solving."
        )
        print("\n=== Comparison Analysis ===")
        print(comparison[:300] + "..." if len(comparison) > 300 else comparison)
    except Exception as e:
        print(f"Error in response comparison: {e}")

if __name__ == "__main__":
    main()
