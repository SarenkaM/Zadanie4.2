def palindrom(word):
    """
    Check is given word palindrom
    Argument: checking word"""
    first_list = []
    for i in word:
        first_list.append(i)
    print(first_list == list(reversed(first_list)))


palindrom("kajak")
palindrom("słowo")
palindrom("123321")
palindrom("potop")

