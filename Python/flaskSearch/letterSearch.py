def search_for_letter(phrase : str, letters : str = 'aeiou'):
    return set(letters).intersection(set(phrase))