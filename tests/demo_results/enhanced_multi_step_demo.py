#!/usr/bin/env python3
"""
Enhanced Multi-Step Reflection Demo: Agentic AI Design Patterns
Uses the improved reflection function with context maintenance, validation, and drift prevention.
"""

import sys
import os
from datetime import datetime

# Add parent directory to path to import reflective_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from reflective_agent import improved_multi_step_reflection

def run_enhanced_demo():
    """Run an enhanced 3-step reflection demo on Agentic AI Design Patterns."""
    
    print("🚀 Enhanced Multi-Step Reflection Demo: Agentic AI Design Patterns")
    print("=" * 80)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # The main prompt
    main_prompt = "Explain the Design Patterns for Agentic AI in detail, including practical examples and implementation considerations."
    
    print("📝 Original Prompt:")
    print(f"'{main_prompt}'")
    print()
    
    print("🔧 Enhanced Features:")
    print("- ✅ Better prompt engineering with context maintenance")
    print("- ✅ Validation checks for relevance and quality")
    print("- ✅ Automatic recovery from off-topic responses")
    print("- ✅ Iteration limits to prevent drift")
    print("- ✅ Real-time scoring and monitoring")
    print()
    
    try:
        # Run enhanced multi-step reflection
        results = improved_multi_step_reflection(main_prompt, steps=3, max_iterations=5)
        
        # Display results
        print("\n" + "=" * 80)
        print("📊 ENHANCED REFLECTION RESULTS")
        print("=" * 80)
        
        print(f"Original Prompt: {len(results['original_prompt'])} characters")
        print(f"Total Iterations: {results['total_iterations']}")
        print(f"Context Maintained: {'✅ Yes' if results['context_maintained'] else '❌ No'}")
        print(f"Validation Passed: {'✅ Yes' if results['validation_passed'] else '❌ No'}")
        print()
        
        # Display each step
        for step in results['steps']:
            print(f"🔄 Step {step['step_number']}:")
            print(f"   Input: {step['input_length']} characters")
            print(f"   Output: {step['output_length']} characters")
            print(f"   Context Score: {step['context_score']:.2f}")
            print(f"   Content Score: {step['content_score']:.2f}")
            print(f"   Validation: {'✅ Passed' if step['validation_passed'] else '❌ Failed'}")
            print()
        
        # Display final response
        print("🎯 FINAL IMPROVED RESPONSE:")
        print("=" * 50)
        print(results['final_response'])
        print("=" * 50)
        
        # Save enhanced results
        save_enhanced_results(results)
        
        print(f"\n📁 Enhanced results saved to: tests/demo_results/enhanced_results/")
        print("🎯 Enhanced demo completed successfully!")
        
    except Exception as e:
        print(f"❌ Enhanced demo failed with error: {e}")
        import traceback
        traceback.print_exc()

def save_enhanced_results(results):
    """Save the enhanced reflection results to files."""
    
    # Create enhanced results directory
    os.makedirs("tests/demo_results/enhanced_results", exist_ok=True)
    
    # Save original prompt
    with open("tests/demo_results/enhanced_results/00_original_prompt.txt", "w", encoding="utf-8") as f:
        f.write(f"Original Prompt:\n{results['original_prompt']}\n")
    
    # Save each step
    for step in results['steps']:
        step_num = step['step_number']
        
        # Save step details
        with open(f"tests/demo_results/enhanced_results/{step_num:02d}_step{step_num}_details.txt", "w", encoding="utf-8") as f:
            f.write(f"STEP {step_num} DETAILS\n")
            f.write("=" * 50 + "\n")
            f.write(f"Input Length: {step['input_length']} characters\n")
            f.write(f"Output Length: {step['output_length']} characters\n")
            f.write(f"Context Score: {step['context_score']:.2f}\n")
            f.write(f"Content Score: {step['content_score']:.2f}\n")
            f.write(f"Validation Passed: {step['validation_passed']}\n\n")
            f.write("INPUT CONTENT:\n")
            f.write("-" * 30 + "\n")
            f.write(step['input_content'])
            f.write("\n\nOUTPUT CONTENT:\n")
            f.write("-" * 30 + "\n")
            f.write(step['output_content'])
        
        # Save just the output content
        with open(f"tests/demo_results/enhanced_results/{step_num:02d}_step{step_num}_output.txt", "w", encoding="utf-8") as f:
            f.write(f"Step {step_num} Output:\n{step['output_content']}\n")
    
    # Save final response
    with open("tests/demo_results/enhanced_results/99_final_response.txt", "w", encoding="utf-8") as f:
        f.write("FINAL ENHANCED RESPONSE\n")
        f.write("=" * 50 + "\n")
        f.write(results['final_response'])
    
    # Save summary
    with open("tests/demo_results/enhanced_results/README.md", "w", encoding="utf-8") as f:
        f.write("# Enhanced Multi-Step Reflection Results\n\n")
        f.write("This folder contains the results of the enhanced multi-step reflection demo.\n\n")
        f.write("## Files:\n\n")
        f.write("- `00_original_prompt.txt` - The original question\n")
        for step in results['steps']:
            step_num = step['step_number']
            f.write(f"- `{step_num:02d}_step{step_num}_details.txt` - Complete step {step_num} details\n")
            f.write(f"- `{step_num:02d}_step{step_num}_output.txt` - Step {step_num} output only\n")
        f.write("- `99_final_response.txt` - Final improved response\n")
        f.write("- `README.md` - This file\n\n")
        f.write("## Results Summary:\n\n")
        f.write(f"- **Original Prompt**: {len(results['original_prompt'])} characters\n")
        f.write(f"- **Total Steps**: {len(results['steps'])}\n")
        f.write(f"- **Context Maintained**: {'Yes' if results['context_maintained'] else 'No'}\n")
        f.write(f"- **Validation Passed**: {'Yes' if results['validation_passed'] else 'No'}\n")
        f.write(f"- **Total Iterations**: {results['total_iterations']}\n\n")
        f.write("## Enhanced Features Used:\n\n")
        f.write("- ✅ Better prompt engineering with context maintenance\n")
        f.write("- ✅ Validation checks for relevance and quality\n")
        f.write("- ✅ Automatic recovery from off-topic responses\n")
        f.write("- ✅ Iteration limits to prevent drift\n")
        f.write("- ✅ Real-time scoring and monitoring\n")

if __name__ == "__main__":
    try:
        run_enhanced_demo()
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        import traceback
        traceback.print_exc()
