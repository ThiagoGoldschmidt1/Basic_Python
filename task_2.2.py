n = input("please type in a number: ")
#Nested loop that starts with 0 and ends with the input +1. Since indeces start with 0, we need the +1 to be able to display all number up to the input
for row in range(0,int(n)+1):
    for column in range(0,int(n)+1):
        # when row == 0 we have to enumerate the column numbers
        if row == 0:
            if column != 0:
                #we use this format when printing to make sure we stay in the same row after printing 
                print(" ", column, end="")
            else:
                # to have that empty space on the left top corner
                print(" ", ' ', end="")
        else:
            # We use the first column to enumerate the rows
            if column == 0:
                print(" ", row, end="")
            # We can test if a number if divisible by another by checking if a % b == 0.
            elif column % row == 0:
                print(" ", 'X', end="")
            else:
                print(" ", " ", end="")
    #Linebreak in the end of the line
    print("\n")
