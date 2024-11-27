import enchant
import re

# Initialize the Danish dictionary
danish_dict = enchant.Dict("da_DK")

def find_spelling_mistakes(text):
    """
    Find spelling mistakes in the text with their positions.

    Args:
        text (str): The input text to check.

    Returns:
        list: A list of dictionaries containing 'word', 'start', and 'end'.
    """
    mistakes = []
    start_index = 0

    # Use regex to split text into words while keeping whitespace and punctuation
    tokens = re.finditer(r'\S+', text)

    for token in tokens:
        word = token.group()
        start = token.start()
        end = token.end()

        # Clean the word of leading/trailing punctuation for spell checking
        cleaned_word = word.strip(".,!?;:()[]\"'")

        # Check if the word is misspelled
        if not danish_dict.check(cleaned_word):
            mistakes.append({
                "word": word,  # Original word with punctuation
                "start": start,
                "end": end
            })

    return mistakes