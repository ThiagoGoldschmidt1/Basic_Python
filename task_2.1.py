
for row in range(3):
    for column in range(3):
        number = row * 3 + column + 1
        print(" ", row, column, end="")


    print("\n")


# 1. It replaces the default linebreak with no charakter. This way the it prints out a full row for each inner loop.
# ("\n") is a linebreak command that indicated the algorythm to proceed to the next row one a cycle of the inner loop is conpleted
#2. The + 1 is necessary since the indexing always starts with 0. If there wasnt a +1 the matrix would still hav ethe same structure but have the range 0-8
