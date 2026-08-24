from app.character_memory import get_character_profile


def generate_prompt(scene, llm_data):

    character_descriptions = []

    for character in scene["characters"]:

        profile = get_character_profile(character)

        description = f"""
{character},
{profile['appearance']},
{profile['clothing']},
{profile['accessories']},
{profile['face']}
"""

        character_descriptions.append(
            description.strip()
        )

    character_text = ", ".join(character_descriptions)

    prompt = f"""
{character_text},

{llm_data['action_detail']},

{llm_data['environment']},

{llm_data['lighting']},

{llm_data['emotion']},

{llm_data['camera']},

highly detailed,
cinematic composition,
Indian mythology illustration,
Amar Chitra Katha style
"""

    return " ".join(prompt.split())