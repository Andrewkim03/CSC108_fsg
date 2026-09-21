# doctest demonstration

def f(x):
    """
    >>> f(10)
    9
    >>> f(11)
    10
    """
    return x

print(f(9))

if __name__ == '__main__':
    import doctest
    doctest.testmod()