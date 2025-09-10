# AI/ML Prompt Library

This directory contains a curated collection of prompts organized by category and use case for various AI models including GPT, Claude, Gemini, and others.

## 📁 Directory Structure

```
prompts/
├── README.md                 # This file
├── categories/              # Prompts organized by category
│   ├── code_generation/     # Code generation and programming
│   ├── text_analysis/       # Text processing and analysis
│   ├── image_generation/    # Image creation prompts
│   ├── data_science/        # Data analysis and ML prompts
│   └── general/             # General purpose prompts
└── templates/               # Reusable prompt templates
```

## 🎯 Categories

### Code Generation
Prompts for generating, reviewing, and explaining code across different programming languages and frameworks.

### Text Analysis
Prompts for analyzing, summarizing, and processing text content including sentiment analysis, extraction, and classification.

### Image Generation
Prompts optimized for text-to-image models like DALL-E, Midjourney, Stable Diffusion, and others.

### Data Science
Specialized prompts for data analysis, machine learning model development, and statistical analysis.

### General
Versatile prompts for common AI tasks including writing, reasoning, and problem-solving.

## 📝 Prompt Format

Each prompt file follows this structure:

```yaml
---
title: "Prompt Title"
category: "category_name"
tags: ["tag1", "tag2", "tag3"]
model_compatibility: ["gpt-4", "claude-3", "gemini-pro"]
difficulty: "beginner|intermediate|advanced"
created_by: "Author Name"
created_at: "2024-01-01"
version: "1.0"
---

# Prompt Title

## Description
Brief description of what this prompt does and when to use it.

## Prompt
```
[The actual prompt content goes here]
```

## Example Usage
```
Input: [Example input]
Output: [Expected output format]
```

## Tips
- Additional tips for using this prompt effectively
- Model-specific considerations
- Parameter recommendations
```

## 🚀 Usage Examples

### Using Prompts with Different Models

#### GPT-4/ChatGPT
```python
import openai

with open("prompts/categories/code_generation/python_function_generator.md") as f:
    prompt = extract_prompt_content(f.read())

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)
```

#### Claude (Anthropic)
```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-3-opus-20240229",
    messages=[{"role": "user", "content": prompt}]
)
```

#### Gemini (Google)
```python
import google.generativeai as genai

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content(prompt)
```

## 📊 Prompt Metrics

Each prompt includes effectiveness metrics when available:
- **Success Rate**: How often the prompt produces desired results
- **Token Efficiency**: Average tokens used vs. output quality
- **Model Compatibility**: Which models work best with this prompt

## 🤝 Contributing

To add a new prompt:

1. Choose the appropriate category directory
2. Create a new `.md` file with a descriptive name
3. Follow the standard format shown above
4. Include relevant tags and compatibility information
5. Test the prompt with multiple models if possible

## 📋 Prompt Guidelines

### Writing Effective Prompts
1. **Be Specific**: Clearly define the task and expected output
2. **Provide Context**: Include relevant background information
3. **Use Examples**: Show the desired input/output format
4. **Set Constraints**: Specify length, format, or style requirements
5. **Test Thoroughly**: Verify prompts work across different models

### Model-Specific Considerations
- **GPT Models**: Excel at creative tasks and detailed instructions
- **Claude**: Strong at analysis and following complex instructions
- **Gemini**: Good for multimodal tasks and reasoning
- **Open Source Models**: May need simpler, more direct prompts

## 📈 Prompt Performance

Track prompt performance using:
- Response quality ratings
- Token usage efficiency
- Model compatibility scores
- User feedback and iterations

## 🔗 Related Resources

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library)
- [Google AI Prompt Guidelines](https://ai.google.dev/docs/prompt_best_practices)

---

*This prompt library is continuously updated with new and improved prompts. Check back regularly for additions and enhancements.*