character_database = {}


def get_character_profile(character_name):

    if character_name in character_database:

        return character_database[character_name]

    # Default generated profile
    profile = generate_default_profile(character_name)

    character_database[character_name] = profile

    return profile


def generate_default_profile(character_name):

    mythology_profiles = {

        "Hanuman": {
            "appearance": "muscular vanara warrior",
            "clothing": "orange dhoti with golden ornaments",
            "accessories": "golden mace",
            "face": "determined expression",
            "style": "Indian mythology illustration"
        },

        "Rama": {
            "appearance": "young prince with blue skin",
            "clothing": "royal yellow garments",
            "accessories": "bow and quiver",
            "face": "calm divine expression",

            "hair": "long dark hair",
            "body_type": "athletic build",
            "age": "young adult",
            "default_pose": "heroic standing pose",
            
            "style": "Indian mythology illustration"
        },

        "Sita": {
            "appearance": "graceful princess",
            "clothing": "traditional royal saree",
            "accessories": "gold jewelry",
            "face": "gentle compassionate expression",
            "style": "Indian mythology illustration"
        }
    }

    return mythology_profiles.get(
        character_name,
        {
            "appearance": "cinematic mythological character",
            "clothing": "traditional ancient attire",
            "accessories": "",
            "face": "expressive face",
            "style": "Indian mythology illustration"
        }
    )