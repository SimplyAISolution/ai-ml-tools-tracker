---
title: "Advanced Sentiment Analysis"
category: "text_analysis" 
tags: ["sentiment", "analysis", "classification", "emotions"]
model_compatibility: ["gpt-4", "claude-3", "gemini-pro"]
difficulty: "intermediate"
created_by: "AI Tools Tracker"
created_at: "2024-01-01"
version: "1.0"
---

# Advanced Sentiment Analysis

## Description
Performs detailed sentiment analysis with emotion detection, confidence scoring, and contextual insights for given text.

## Prompt
```
Analyze the sentiment of the following text and provide a comprehensive breakdown:

**Text to analyze**: "{text_content}"

Please provide your analysis in the following format:

## Sentiment Analysis Results

### Overall Sentiment
- **Primary Sentiment**: [Positive/Negative/Neutral]
- **Confidence Score**: [0-100]%
- **Sentiment Strength**: [Weak/Moderate/Strong]

### Emotional Breakdown
- **Primary Emotion**: [Joy/Anger/Fear/Sadness/Surprise/Disgust/Trust/Anticipation]
- **Secondary Emotions**: [List up to 3]
- **Emotional Intensity**: [Low/Medium/High]

### Detailed Analysis
- **Key Sentiment Indicators**: [Words/phrases that influenced the sentiment]
- **Context Considerations**: [Any contextual factors affecting interpretation]
- **Tone Characteristics**: [Formal/Informal, Serious/Casual, etc.]

### Confidence Factors
- **High Confidence Indicators**: [Clear sentiment signals]
- **Uncertainty Factors**: [Ambiguous elements, if any]

Provide reasoning for your analysis and note any sarcasm, irony, or complex sentiment patterns detected.
```

## Example Usage
```
Input: "I absolutely love this new AI tool! It's incredibly efficient and saves me hours of work every day. However, I'm a bit concerned about the learning curve for my team members who are less tech-savvy."

Output:
## Sentiment Analysis Results

### Overall Sentiment
- **Primary Sentiment**: Positive
- **Confidence Score**: 75%
- **Sentiment Strength**: Moderate

### Emotional Breakdown
- **Primary Emotion**: Joy
- **Secondary Emotions**: Trust, Anticipation, Concern
- **Emotional Intensity**: Medium

### Detailed Analysis
- **Key Sentiment Indicators**: "absolutely love", "incredibly efficient", "saves me hours", "concerned"
- **Context Considerations**: Mixed sentiment with enthusiasm tempered by practical concerns
- **Tone Characteristics**: Professional, genuine, balanced

### Confidence Factors
- **High Confidence Indicators**: Strong positive language ("absolutely love", "incredibly")
- **Uncertainty Factors**: Contrasting concern about team adoption creates complexity
```

## Tips
- Works best with substantial text (50+ words) for accurate analysis
- Consider cultural context when analyzing sentiment
- Ask for specific aspects if analyzing product reviews or feedback
- Request comparison analysis when evaluating multiple texts
- Specify if you need sentiment trends over time for multiple texts