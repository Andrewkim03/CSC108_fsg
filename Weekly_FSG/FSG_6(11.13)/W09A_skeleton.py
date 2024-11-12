from typing import Any, TextIO
from random import choice, randint


def random_element(lst: list[Any]) -> Any:
    """
    Return a random element of non-empty <lst>.
    """

    return lst[randint(0, len(lst) - 1)]


# TASK 1: Modify from W09A
def associate_pair(d: dict[str, list[str]], key: str, value: str):
    """
    Add the <key>-<value> pair to <d>. Keys may need to be
    associated with multiple values, so values are placed in a list.

    Assumption: key is immutable.
    """

    # TODO 
    pass


# TASK 1: Modify from W09A
def make_dictionary(f: TextIO) -> dict[tuple[str], list[str]]:
    """
    Return a dictionary where the keys are tuples of length 3
    containing words in <f> and the value for a key is the
    list of words that were found to follow the key in <f>.
    """

    # TODO 
    pass


# TASK 1: Modify from W09A
def mimic_text(word_dict: dict[tuple[str], list[str]], num_words: int) -> str:
    """
    Based on the word patterns in <word_dict>, return a string of length
    <num_words> that mimics that text.
    """

    # TODO 
    pass


if __name__ == '__main__':
    with open('seuss1.txt', 'r') as f:   # try changing text files!
        word_d = make_dictionary(f)
    print(mimic_text(word_d, 100))       # test different <num_words> lengths!
