def palindrom(word):
    """
    Check is given word palindrom
    Argument: checking word"""
    first_list = []
    for i in word:
        first_list.append(i)
    print(first_list == list(reversed(first_list)))

def palindrom_easy(word):
    """
    Check is given word palindrom
    Argument: checking word"""
    first_list = []
    print(word[::1] == word[::-1])


palindrom("kajak")
palindrom("słowo")
palindrom("123321")
palindrom("potop")

palindrom_easy("kajak")
palindrom_easy("słowo")
palindrom_easy("123321")
palindrom_easy("potop")