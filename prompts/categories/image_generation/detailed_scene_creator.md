---
title: "Detailed Scene Creator"
category: "image_generation"
tags: ["scene", "detailed", "composition", "lighting", "style"]
model_compatibility: ["dalle-3", "midjourney", "stable-diffusion", "leonardo"]
difficulty: "advanced"
created_by: "AI Tools Tracker"
created_at: "2024-01-01"
version: "1.0"
---

# Detailed Scene Creator

## Description
Creates comprehensive, detailed prompts for generating complex scenes with specific artistic styles, lighting, and compositional elements.

## Prompt
```
Create a detailed image generation prompt for the following scene:

**Base Scene**: {scene_description}
**Art Style**: {art_style} (e.g., photorealistic, digital art, oil painting, etc.)
**Mood/Atmosphere**: {mood}
**Key Elements**: {key_elements}

Generate a comprehensive prompt that includes:

### Technical Specifications
- **Composition**: [Rule of thirds, symmetry, etc.]
- **Lighting**: [Golden hour, dramatic shadows, soft diffused, etc.]
- **Camera Angle**: [Eye level, bird's eye, worm's eye, etc.]
- **Depth of Field**: [Shallow, deep focus, specific focus areas]

### Visual Details
- **Color Palette**: [Dominant colors and mood]
- **Textures**: [Surface materials and finishes]
- **Environmental Details**: [Weather, time of day, season]
- **Character Details**: [If applicable - clothing, expressions, poses]

### Quality Modifiers
- **Resolution**: [4K, 8K, high detail specifications]
- **Artistic References**: [Specific artists or movements if relevant]
- **Technical Terms**: [Relevant photography/art terminology]

Format as a single, optimized prompt ready for image generation models.
```

## Example Usage
```
Input:
- Base Scene: A cozy coffee shop on a rainy evening
- Art Style: Cinematic photography
- Mood: Warm and inviting
- Key Elements: Steaming coffee, rain on windows, soft lighting

Output:
A cozy coffee shop interior during a rainy evening, cinematic photography style, warm amber lighting from vintage Edison bulbs casting soft shadows, rain droplets streaming down large windows creating bokeh effects, steaming coffee cup in foreground with latte art, weathered wooden tables with books and newspapers scattered, barista in soft focus background, golden hour color palette with deep blues and warm oranges, shallow depth of field focusing on the coffee cup, shot with 85mm lens, professional photography lighting, atmospheric mist from hot beverages, reflections on wet surfaces, cozy blankets draped over chairs, vintage coffee equipment, film grain texture, moody and intimate atmosphere, hyperrealistic detail, 4K resolution
```

## Tips
- Layer details progressively (main subject → environment → lighting → technical)
- Use specific photography terms for realistic images
- Include negative prompts for unwanted elements
- Adjust complexity based on the model's capabilities
- Test with different aspect ratios for composition variety
- Consider style-specific terminology (e.g., "trending on ArtStation" for digital art)