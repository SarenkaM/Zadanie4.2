def palindrom_easy(word):
    """
    Check is given word palindrom
    Argument: checking word"""
    palindrom = True
    if word == word[::-1]:
        return True
    else:
        return False


print(palindrom_easy(("kajak")))
print(palindrom_easy(("kajaki")))


