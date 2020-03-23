from string import ascii_lowercase

def is_pangram(sentence):
    alphabet = list(ascii_lowercase)
    for letter in sentence.lower():
        if not alphabet: # Break loop if all letters used.
            break
        if letter in alphabet:
            alphabet.remove(letter)
    if alphabet:
        return False
    else:
        return True
