def uppercase(str):
    g = ""
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            g = g + chr((ord(str[i]) - 32))
        else:
            g = g + str[i]

    print("{}".format(g), end="")
    print()
