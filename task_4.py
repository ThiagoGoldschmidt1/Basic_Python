from random import randint

def x_or_o(probability_of_x):
    if randint(1, 10) <= probability_of_x*10:
        return "X"
    else:
        return "O"

def random_string(n):
    for num in range(n):
        print("", x_or_o(0.7), end ='')

random_string(70)
