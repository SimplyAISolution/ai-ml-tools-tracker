---
title: "Python Function Generator"
category: "code_generation"
tags: ["python", "function", "documentation", "testing"]
model_compatibility: ["gpt-4", "claude-3", "gemini-pro", "codellama"]
difficulty: "beginner"
created_by: "AI Tools Tracker"
created_at: "2024-01-01"
version: "1.0"
---

# Python Function Generator

## Description
Generates well-documented Python functions with type hints, docstrings, and basic error handling based on a functional description.

## Prompt
```
Create a Python function based on the following requirements:

**Function Description**: {function_description}
**Input Parameters**: {input_parameters}
**Expected Output**: {expected_output}
**Additional Requirements**: {additional_requirements}

Please provide:
1. A complete Python function with proper type hints
2. A comprehensive docstring following Google/NumPy style
3. Basic error handling where appropriate
4. Simple usage examples
5. Any necessary import statements

Format the response as clean Python code with comments explaining the logic.
```

## Example Usage
```
Input: 
- Function Description: Calculate compound interest
- Input Parameters: principal (float), rate (float), time (int), compound_frequency (int)
- Expected Output: final amount (float)
- Additional Requirements: Validate input parameters are positive

Output:
```python
from typing import Union

def calculate_compound_interest(
    principal: float, 
    rate: float, 
    time: int, 
    compound_frequency: int = 12
) -> float:
    """
    Calculate compound interest for a given principal amount.
    
    Args:
        principal: Initial amount of money
        rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        time: Time period in years
        compound_frequency: Number of times interest compounds per year
    
    Returns:
        Final amount after compound interest
    
    Raises:
        ValueError: If any parameter is not positive
    """
    if principal <= 0 or rate <= 0 or time <= 0 or compound_frequency <= 0:
        raise ValueError("All parameters must be positive")
    
    final_amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    return round(final_amount, 2)

# Usage example
amount = calculate_compound_interest(1000, 0.05, 5, 12)
print(f"Final amount: ${amount}")
```
```

## Tips
- Be specific about parameter types and constraints
- Request examples to understand the expected behavior
- Specify coding standards (PEP 8, type hints, docstring style)
- Ask for error handling appropriate to the function's complexity
- Consider asking for unit tests for critical functions