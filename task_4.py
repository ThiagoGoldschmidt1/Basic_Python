from random import randint

#x_or_o returns either X or O and takes as a parameter the probability of X
def x_or_o(probability_of_x):
    #if our randomint is smaller than our probability times 10, it returns X (prob 0.7*10 = 7, so if our randint is 1-7 returns X)
    if randint(1, 10) <= probability_of_x*10:
        return "X"
    else:
        return "O"

#prints a string with random occurences of X or O with length n
def random_string(n):
    for num in range(n):
        #uses our predefines x_or_o function to randomly print an X or O in each iteratrion
        print("", x_or_o(0.7), end ='')

random_string(70)
