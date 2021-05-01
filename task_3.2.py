def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2,n-1):
            if n % i != 0:
                continue
            else:
                return False

        return True

num = int(input('Please input a numnber: '))

def prime_detector(num):
    for number in range(1,num +1):
        if is_prime(number) == True:
            print(f"{number} is a prime.")
        else:
            print(f"{number} is not a prime.")

prime_detector(num)
