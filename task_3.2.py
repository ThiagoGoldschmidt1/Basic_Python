# This function chekcs if a number is prime
def is_prime(n):
    #1 isnt a prime number, but its kind of an exeption to the rule
    if n == 1:
        return False
    else:
    #Checks in the range from 2 to our n -1
        for i in range(2,n-1):
            #If it is not divisible by this number
            if n % i != 0:
                #check the next one
                continue
            else:
                #if it is divisible, its not a prime number
                return False
        #If it went through the whole range wihtout finding one number that it is divisible by, its a prime number
        return True

#takes an input and turns it into an integer so we can use it inour function
num = int(input('Please input a numnber: '))


def prime_detector(num):
    #checks in this range, starts with 1 since we dont want to check 0
    for number in range(1,num +1):
        if is_prime(number) == True:
            print(f"{number} is a prime.")
        else:
            print(f"{number} is not a prime.")

prime_detector(num)
