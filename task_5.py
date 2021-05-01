random_nr = randint(1, 100)
#Turns input into an integeer since input are strings as default
guess = int(input("Guess a number: "))
#A variable that keeps track of the amoutn of guesses we made
nr_of_guesses = 0

# Keeps asking while we dont have the right number
while guess != random_nr:
    #if its bigger:
    if random_nr > guess:
        print('My number is bigger than that')
        #asks for a new input
        guess = int(input("Guess a number: "))
        #keeps track of the amount of guesses
        nr_of_guesses += 1
    elif random_nr < guess:
        print('My number is smaller than that')
        guess = int(input("Guess a number: "))
        nr_of_guesses += 1
#If our while condition is met, meaning we guessed the right number, this is displayed
print(f'Nice you got it and it took you only {nr_of_guesses} attempts')
