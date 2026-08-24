import requests
import json
from app.text_cleaner import clean_text

OLLAMA_URL = "http://localhost:11434/api/generate"


def enrich_scene_with_llm(scene, original_text):

    prompt = f"""
You are a cinematic visual scene generator.

Analyze the story scene and generate vivid cinematic details
for AI image generation.

Scene Text:
{original_text}

Known Scene Context:
Characters: {scene['characters']}
Location: {scene['location']}
Action: {scene['action']}
Mood: {scene['mood']}

Return ONLY valid JSON.

Use this EXACT structure:

{{
    "environment": "rich cinematic environment description",
    "lighting": "cinematic lighting description",
    "camera": "camera shot description",
    "emotion": "emotional atmosphere",
    "action_detail": "detailed cinematic action"
}}

Rules:
- Use simple cinematic language.
- Keep every value under 12 words.
- Avoid poetic writing.
- Avoid repetition.
- Avoid unusual words.
- Do not leave fields empty.
- Focus on visual descriptions only.
- Camera descriptions must be short cinematic shot types.
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
        "format": "json",

        "options": {
            "temperature": 0.3,
            "top_p": 0.8,
            "num_predict": 120
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )

        result = response.json()

        raw_output = result["response"].strip()

        print("\nRAW LLM OUTPUT:\n")
        print(raw_output)

        enriched_data = json.loads(raw_output)

        required_keys = [
            "environment",
            "lighting",
            "camera",
            "emotion",
            "action_detail"
        ]

        cleaned_data = {}

        for key, value in enriched_data.items():
            cleaned_key = key.strip().lower()

            if cleaned_key in required_keys:
                cleaned_data[cleaned_key] = value
        
        enriched_data = cleaned_data

        fallback_values = {
            "environment": "cinematic mythological environment",
            "lighting": "dramatic cinematic lighting",
            "camera": "wide cinematic shot",
            "emotion": "epic mythological atmosphere",
            "action_detail": "dynamic cinematic action"
        }

        for key in required_keys:

            if key not in enriched_data:
                enriched_data[key] = fallback_values[key]

            if not enriched_data[key].strip():
                enriched_data[key] = fallback_values[key]

            enriched_data[key] = clean_text(
                enriched_data[key]
            )

        return enriched_data

    except Exception as e:

        print("\nLLM ERROR:")
        print(e)

        return {
            "environment": "cinematic mythological environment",
            "lighting": "dramatic cinematic lighting",
            "camera": "wide cinematic shot",
            "emotion": "epic mythological atmosphere",
            "action_detail": "dynamic cinematic action"
        }