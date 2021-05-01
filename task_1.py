some_number = 42

while some_number < 100:
    print("Look at my number:", some_number)
    some_number += 1



for i in range(some_number, 100):
    if some_number < 100:
        print("Look at my number:", some_number)
        some_number += 1
    else:
        break



subtractor = 10
for i in range(10, 21, 2):
  some_number -= i
  print(some_number)

while subtractor < (21):
    some_number -= subtractor
    subtractor += 2
    print(some_number)
