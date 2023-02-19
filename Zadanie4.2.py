def palindrom_easy(word):
    """
    Check is given word palindrom
    Argument: checking word"""
    return word == word[::-1]




print(palindrom_easy(("kajak")))
print(palindrom_easy(("kajaki")))
print(palindrom_easy(("kkajakk")))


