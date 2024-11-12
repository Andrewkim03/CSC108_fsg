from typing import TextIO
from random import choice


# Task 1
def make_dictionary(filename: str) -> dict[str, list[str]]:
    """
    Return a dictionary where the keys are words in <filename> and the value
    for a key is the list of words that were found to follow the key.
    """

    # TODO 
    pass


# Task 2
def mimic_text(word_dict: dict[str, list[str]], num_words: int) -> str:
    """
    Based on the word patterns in <word_dict>, return a string with
    <num_words> words that mimics the text.
    """

    # TODO 
    pass


if __name__ == '__main__':

    word_d = make_dictionary('seuss1.txt')  # try changing text files!
    print(mimic_text(word_d, 100))          # test different <num_words> lengths!
