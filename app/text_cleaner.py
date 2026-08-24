import re


def clean_text(text):

    if not text:
        return ""

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove repeated character patterns
    text = re.sub(r'(\w+)\1+', r'\1', text)

    # Remove broken duplicated syllables
    text = re.sub(r'([A-Za-z]{2,})\1', r'\1', text)

    # Remove weird punctuation
    text = re.sub(r'[^\w\s,.-]', '', text)

    # Cleanup repeated words
    words = text.split()

    cleaned_words = []

    for word in words:

        if (
            len(cleaned_words) == 0
            or cleaned_words[-1].lower() != word.lower()
        ):
            cleaned_words.append(word)

    text = " ".join(cleaned_words)

    return text.strip()