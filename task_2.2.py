n = input("please type in a number: ")

for row in range(0,int(n)+1):
    for column in range(0,int(n)+1):
        if row == 0:
            if column != 0:
                print(" ", column, end="")
            else:
                print(" ", ' ', end="")
        else:
            if column == 0:
                print(" ", row, end="")
            elif column % row == 0:
                print(" ", 'X', end="")
            else:
                print(" ", " ", end="")

    print("\n")
