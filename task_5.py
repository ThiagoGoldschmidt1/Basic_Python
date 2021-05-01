random_nr = randint(1, 100)
guess = int(input("Guess a number: "))
nr_of_guesses = 0

while guess != random_nr:
    if random_nr > guess:
        print('My number is bigger than that')
        guess = int(input("Guess a number: "))
        nr_of_guesses += 1
    elif random_nr < guess:
        print('My number is smaller than that')
        guess = int(input("Guess a number: "))
        nr_of_guesses += 1

print(f'Nice you got it and it took you only {nr_of_guesses} attempts')
