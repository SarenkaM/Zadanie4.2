def palindrom(x):
    first_list = []
    for i in x:
        first_list.append(i)
    print(first_list == list(reversed(first_list)))


palindrom("kajak")
palindrom("słowo")
palindrom("123321")
palindrom("potop")

