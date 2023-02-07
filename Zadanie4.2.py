

def palindrom_easy(word):
    """
    Check is given word palindrom
    Argument: checking word"""
    palindrom = True
    if word == word[::-1]:
        print(palindrom)
    else:
        print(bool())




palindrom_easy("kajak")
palindrom_easy("słowo")
palindrom_easy("123321")
palindrom_easy("potop")
palindrom_easy("pottop")