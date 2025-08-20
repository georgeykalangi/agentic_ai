#!/usr/bin/env python3
"""
Temporary Demo Script: Multi-Step Reflection on Agentic AI Design Patterns
Demonstrates 3-step reflection with progressive improvement and comparison.
"""

import sys
import os
from datetime import datetime

# Add parent directory to path to import reflective_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from reflective_agent import reflect_and_improve, compare_responses

def run_multi_step_demo():
    """Run a 3-step reflection demo on Agentic AI Design Patterns."""
    
    print("🚀 Multi-Step Reflection Demo: Agentic AI Design Patterns")
    print("=" * 70)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # The main prompt
    main_prompt = "Explain the Design Patterns for Agentic AI in detail, including practical examples and implementation considerations."
    
    print("📝 Original Prompt:")
    print(f"'{main_prompt}'")
    print()
    
    # Step 1: Initial response
    print("🔄 Step 1: Initial Response Generation")
    print("-" * 50)
    initial_response, step1_improved = reflect_and_improve(main_prompt)
    
    print(f"Initial Response Length: {len(initial_response)} characters")
    print(f"Step 1 Improved Length: {len(step1_improved)} characters")
    print()
    
    # Step 2: Second reflection
    print("🔄 Step 2: Second Reflection Cycle")
    print("-" * 50)
    step2_input, step2_improved = reflect_and_improve(step1_improved)
    
    print(f"Step 2 Input Length: {len(step2_input)} characters")
    print(f"Step 2 Improved Length: {len(step2_improved)} characters")
    print()
    
    # Step 3: Third reflection
    print("🔄 Step 3: Final Reflection Cycle")
    print("-" * 50)
    step3_input, final_response = reflect_and_improve(step2_improved)
    
    print(f"Step 3 Input Length: {len(step3_input)} characters")
    print(f"Final Response Length: {len(final_response)} characters")
    print()
    
    # Save all results to files
    save_results(main_prompt, initial_response, step1_improved, step2_improved, final_response)
    
    # Generate comparison analysis
    print("📊 Generating Comparison Analysis...")
    comparison, improved_comparison = compare_responses(initial_response, final_response)
    
    # Save comparison
    save_comparison(comparison, improved_comparison)
    
    # Display summary
    print("\n" + "=" * 70)
    print("📈 REFLECTION PROGRESS SUMMARY")
    print("=" * 70)
    print(f"Original Prompt Length: {len(main_prompt)} characters")
    print(f"Initial Response: {len(initial_response)} characters")
    print(f"After Step 1: {len(step1_improved)} characters (+{len(step1_improved) - len(initial_response)})")
    print(f"After Step 2: {len(step2_improved)} characters (+{len(step2_improved) - len(step1_improved)})")
    print(f"Final Response: {len(final_response)} characters (+{len(final_response) - len(initial_response)} total)")
    print()
    print(f"📁 Results saved to: tests/demo_results/")
    print("🎯 Demo completed successfully!")

def save_results(prompt, initial, step1, step2, final):
    """Save all reflection results to separate files."""
    
    # Save original prompt
    with open("tests/demo_results/00_original_prompt.txt", "w", encoding="utf-8") as f:
        f.write(f"Original Prompt:\n{prompt}\n")
    
    # Save initial response
    with open("tests/demo_results/01_initial_response.txt", "w", encoding="utf-8") as f:
        f.write(f"Initial Response:\n{initial}\n")
    
    # Save step 1 improved
    with open("tests/demo_results/02_step1_improved.txt", "w", encoding="utf-8") as f:
        f.write(f"Step 1 Improved Response:\n{step1}\n")
    
    # Save step 2 improved
    with open("tests/demo_results/03_step2_improved.txt", "w", encoding="utf-8") as f:
        f.write(f"Step 2 Improved Response:\n{step2}\n")
    
    # Save final response
    with open("tests/demo_results/04_final_response.txt", "w", encoding="utf-8") as f:
        f.write(f"Final Response (After 3 Steps):\n{final}\n")
    
    # Save combined results
    with open("tests/demo_results/05_all_steps_combined.txt", "w", encoding="utf-8") as f:
        f.write("MULTI-STEP REFLECTION DEMO: AGENTIC AI DESIGN PATTERNS\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"ORIGINAL PROMPT:\n{prompt}\n\n")
        f.write(f"STEP 1 - INITIAL RESPONSE:\n{initial}\n\n")
        f.write(f"STEP 2 - FIRST IMPROVEMENT:\n{step1}\n\n")
        f.write(f"STEP 3 - SECOND IMPROVEMENT:\n{step2}\n\n")
        f.write(f"FINAL - THIRD IMPROVEMENT:\n{final}\n\n")
        f.write("=" * 70 + "\n")
        f.write("Demo completed successfully!\n")

def save_comparison(comparison, improved_comparison):
    """Save the comparison analysis."""
    
    with open("tests/demo_results/06_comparison_analysis.txt", "w", encoding="utf-8") as f:
        f.write("COMPARISON ANALYSIS: INITIAL vs FINAL RESPONSE\n")
        f.write("=" * 50 + "\n\n")
        f.write("AI-GENERATED COMPARISON:\n")
        f.write(comparison)
        f.write("\n\n" + "=" * 50 + "\n")
        f.write("IMPROVED COMPARISON:\n")
        f.write(improved_comparison)

if __name__ == "__main__":
    try:
        run_multi_step_demo()
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()
