import spacy


nlp = spacy.load("en_core_web_lg")


def calculate_embedding(input_word):
    """
    Return the spaCy embedding vector for the input word.

    This follows the Module 2 Practical 3 implementation:
        word = nlp(input_word)
        return word.vector
    """
    word = nlp(input_word)
    return word.vector
