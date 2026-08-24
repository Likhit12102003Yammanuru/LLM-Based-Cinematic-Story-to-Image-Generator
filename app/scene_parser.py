import spacy

nlp = spacy.load("en_core_web_sm")

MYTHOLOGY_NAMES = [
    "Rama",
    "Sita",
    "Hanuman",
    "Krishna",
    "Arjuna",
    "Lakshmana",
    "Ravana"
]

LOCATION_WORDS = [
    "ocean",
    "forest",
    "palace",
    "battlefield",
    "river",
    "mountain",
    "temple",
    "kingdom",
    "hall"
]

MOOD_WORDS = {
    "dark": "mysterious",
    "night": "dramatic",
    "sunset": "peaceful",
    "battle": "tense",
    "war": "intense",
    "rain": "melancholic"
}


def parse_scene(text):

    doc = nlp(text)

    characters = []
    action = ""
    location = ""
    mood = "cinematic"

    # Character extraction
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            characters.append(ent.text)

    for token in doc:
        if token.text in MYTHOLOGY_NAMES:
            if token.text not in characters:
                characters.append(token.text)

    # Action extraction
    for token in doc:
        if token.pos_ == "VERB":
            action = token.lemma_
            break

    # Location extraction
    for token in doc:
        if token.text.lower() in LOCATION_WORDS:
            location = token.text.lower()
            break

    # Mood inference
    for token in doc:
        if token.text.lower() in MOOD_WORDS:
            mood = MOOD_WORDS[token.text.lower()]

    # Fallbacks
    if not characters:
        characters.append("Unknown Character")

    if not action:
        action = "standing"

    if not location:
        location = "cinematic environment"

    return {
        "characters": characters,
        "action": action,
        "location": location,
        "mood": mood
    }