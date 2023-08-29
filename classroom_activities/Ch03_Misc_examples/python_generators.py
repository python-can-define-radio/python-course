mynames = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer"]

def hasMoreThanSixLetters(word):
    if len(word) > 6:
        return True
    else:
        return False


print(hasMoreThanSixLetters("Bob"))
print(hasMoreThanSixLetters("SLKDfdlkjfl"))

longNames = list(filter(hasMoreThanSixLetters, mynames))
print(longNames)


def myfilter(func, iterable):
    """This is not identical to the built-in filter function,
    but it is quite similar."""
    for item in iterable:
        if func(item) == True:
            yield item


longNames = list(myfilter(hasMoreThanSixLetters, mynames))
print(longNames)
