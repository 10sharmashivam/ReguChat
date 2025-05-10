def check_compliance(text, banned_words=["lawsuit", "fraud"]):
    """
    Checks if a given text complies with a given list of banned words.
    
    This function is case-insensitive and returns True if the text is compliant
    and False otherwise.
    
    Parameters:
        text (str): the text to check
        banned_words (list): a list of banned words
    """
    return not any(word in text.lower() for word in banned_words)