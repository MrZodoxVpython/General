for i in range(5):
    for j in range(5):
        if i == 0 or j == 4 or (i == 4 and j >=4 - i):
            print("*", end="")
        if i == 0 or j == 4 or (i == 4 and j >=4 - i):
            print("*", end="")
        else:
            print("  ", end="")
    print()