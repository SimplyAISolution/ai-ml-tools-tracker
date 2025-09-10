---
title: "Basic Prompt Template"
category: "templates"
tags: ["template", "basic", "structure"]
model_compatibility: ["universal"]
difficulty: "beginner"
created_by: "AI Tools Tracker"
created_at: "2024-01-01"
version: "1.0"
---

# Basic Prompt Template

## Description
A fundamental template structure for creating effective prompts across different AI models and use cases.

## Template Structure
```
## Context Setting
You are a {role/expertise} with {relevant_background}. 

## Task Definition
Your task is to {specific_action} based on the following information:

**Input**: {input_description}
**Requirements**: {specific_requirements}
**Output Format**: {desired_output_format}

## Additional Instructions
- {instruction_1}
- {instruction_2}
- {instruction_3}

## Examples (Optional)
Input: {example_input}
Output: {example_output}

## Constraints
- {constraint_1}
- {constraint_2}

Please {final_instruction_or_call_to_action}.
```

## Variables to Customize
- `{role/expertise}`: Specify the AI's role (e.g., "data scientist", "creative writer", "code reviewer")
- `{relevant_background}`: Add context about expertise level or domain knowledge
- `{specific_action}`: Clear verb describing what you want done
- `{input_description}`: What you'll provide as input
- `{specific_requirements}`: Detailed specifications for the output
- `{desired_output_format}`: Structure, length, style preferences
- `{instruction_N}`: Step-by-step guidance or important considerations
- `{example_input/output}`: Concrete examples to clarify expectations
- `{constraint_N}`: Limitations or things to avoid
- `{final_instruction}`: Clear call to action

## Usage Tips
1. **Start Simple**: Begin with the core template and add complexity as needed
2. **Be Specific**: The more precise your instructions, the better the output
3. **Provide Context**: Help the AI understand the domain and purpose
4. **Use Examples**: Show rather than just tell when possible
5. **Set Constraints**: Define what you don't want as clearly as what you do want
6. **Iterate**: Refine the prompt based on initial outputs

## Example Implementation
```
## Context Setting
You are a professional email writer with expertise in business communication.

## Task Definition
Your task is to compose a professional follow-up email based on the following information:

**Input**: Meeting notes and action items
**Requirements**: Professional tone, clear action items, appropriate length
**Output Format**: Complete email with subject line, greeting, body, and closing

## Additional Instructions
- Use a friendly but professional tone
- Include specific deadlines for action items
- Reference key discussion points from the meeting
- Keep the email concise (under 200 words)

## Constraints
- Avoid overly casual language
- Don't include confidential details
- Ensure all action items have clear ownership

Please write the complete follow-up email ready to send.
```

## Variations by Model
### For GPT Models
- Can handle longer, more complex instructions
- Responds well to role-playing scenarios
- Benefits from clear format specifications

### For Claude
- Excels with structured, logical prompts
- Works well with step-by-step breakdowns
- Appreciates explicit reasoning requests

### For Gemini
- Handles multimodal instructions well
- Good with comparative analysis requests
- Effective with creative constraints

### For Open Source Models
- Keep instructions simple and direct
- Use fewer variables and conditions
- Provide more explicit examples