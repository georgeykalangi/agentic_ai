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

def improved_multi_step_reflection(prompt, steps=3, model="gemini-2.0-flash", max_iterations=5):
    """
    Enhanced multi-step reflection with better prompt engineering, context maintenance, 
    validation checks, and iteration limits to prevent drift.
    
    Args:
        prompt (str): The initial prompt for the model
        steps (int): Number of reflection cycles to perform
        model (str): The model to use
        max_iterations (int): Maximum iterations to prevent infinite loops
    
    Returns:
        dict: Complete reflection results with validation and context tracking
    """
    # Get API key from environment variable for security
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. Please create a .env file with your API key.")
    
    client = genai.Client(api_key=api_key)
    
    results = {
        'original_prompt': prompt,
        'steps': [],
        'final_response': '',
        'context_maintained': True,
        'validation_passed': True,
        'total_iterations': 0
    }
    
    current_response = prompt
    iteration_count = 0
    
    for step_num in range(1, steps + 1):
        print(f"🔄 Step {step_num}/{steps}: Enhanced Reflection with Context Maintenance...")
        
        # Enhanced reflection prompt with context maintenance
        enhanced_reflection_prompt = f"""
IMPORTANT: You are improving a response about the following topic. STAY ON TOPIC and maintain context.

ORIGINAL TOPIC: {prompt}

CURRENT RESPONSE TO IMPROVE:
{current_response}

TASK: Improve this response while:
1. MAINTAINING the original topic and context
2. ENHANCING clarity, structure, and usefulness
3. ADDING relevant examples and practical details
4. KEEPING the response focused and well-organized

DO NOT:
- Change the subject matter
- Start analyzing feedback about improving documents
- Go off-topic
- Lose the original context

Provide ONLY the improved response content, not analysis or feedback.
"""
        
        try:
            # Generate improved response
            reflection_response = client.models.generate_content(
                model=model,
                contents=enhanced_reflection_prompt
            )
            improved_response = reflection_response.text
            
            # Context validation check
            context_score = validate_context_maintenance(prompt, improved_response)
            
            # Content validation check
            content_score = validate_content_quality(improved_response)
            
            # If validation fails, try to recover
            if context_score < 0.7 or content_score < 0.6:
                print(f"⚠️  Validation failed in step {step_num}. Attempting recovery...")
                
                recovery_prompt = f"""
The previous improvement went off-topic. Please provide a focused improvement of this response:

ORIGINAL TOPIC: {prompt}
CURRENT RESPONSE: {current_response}

IMPROVE this response while staying strictly on the topic of {prompt}.
Focus on enhancing clarity, adding examples, and improving structure.
"""
                
                recovery_response = client.models.generate_content(
                    model=model,
                    contents=recovery_prompt
                )
                improved_response = recovery_response.text
                
                # Re-validate after recovery
                context_score = validate_context_maintenance(prompt, improved_response)
                content_score = validate_content_quality(improved_response)
            
            # Store step results
            step_result = {
                'step_number': step_num,
                'input_length': len(current_response),
                'output_length': len(improved_response),
                'context_score': context_score,
                'content_score': content_score,
                'input_content': current_response,
                'output_content': improved_response,
                'validation_passed': context_score >= 0.7 and content_score >= 0.6
            }
            
            results['steps'].append(step_result)
            current_response = improved_response
            iteration_count += 1
            
            print(f"✅ Step {step_num} completed:")
            print(f"   Input: {step_result['input_length']} chars → Output: {step_result['output_length']} chars")
            print(f"   Context Score: {context_score:.2f}, Content Score: {content_score:.2f}")
            
            # Check iteration limit
            if iteration_count >= max_iterations:
                print(f"⚠️  Reached maximum iterations ({max_iterations}). Stopping to prevent drift.")
                break
                
        except Exception as e:
            print(f"❌ Error in step {step_num}: {e}")
            # Use previous response if current step fails
            break
    
    results['final_response'] = current_response
    results['total_iterations'] = iteration_count
    results['context_maintained'] = all(step['validation_passed'] for step in results['steps'])
    results['validation_passed'] = results['context_maintained']
    
    return results

def validate_context_maintenance(original_prompt, response):
    """
    Validate that the response maintains context with the original prompt.
    
    Args:
        original_prompt (str): The original prompt
        response (str): The response to validate
    
    Returns:
        float: Context relevance score (0.0 to 1.0)
    """
    # Simple keyword-based validation
    original_keywords = extract_keywords(original_prompt.lower())
    response_keywords = extract_keywords(response.lower())
    
    if not original_keywords:
        return 1.0
    
    # Calculate overlap
    common_keywords = original_keywords.intersection(response_keywords)
    relevance_score = len(common_keywords) / len(original_keywords)
    
    return min(relevance_score * 1.5, 1.0)  # Boost score slightly

def validate_content_quality(response):
    """
    Validate the quality of the response content.
    
    Args:
        response (str): The response to validate
    
    Returns:
        float: Content quality score (0.0 to 1.0)
    """
    if not response or len(response.strip()) < 50:
        return 0.0
    
    # Check for common off-topic indicators
    off_topic_phrases = [
        'feedback', 'suggestion', 'improve the document', 'revise the',
        'thank you for the feedback', 'this response is excellent',
        'minor suggestions', 'why this revised response'
    ]
    
    response_lower = response.lower()
    off_topic_count = sum(1 for phrase in off_topic_phrases if phrase in response_lower)
    
    # Penalize off-topic content
    if off_topic_count > 0:
        return max(0.0, 1.0 - (off_topic_count * 0.3))
    
    return 1.0

def extract_keywords(text):
    """Extract meaningful keywords from text."""
    # Remove common words and extract key terms
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}
    
    words = text.split()
    keywords = set()
    
    for word in words:
        word = word.strip('.,!?;:()[]{}"\'').lower()
        if len(word) > 3 and word not in stop_words:
            keywords.add(word)
    
    return keywords

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
