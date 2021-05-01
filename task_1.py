some_number = 42

while some_number < 100:
    print("Look at my number:", some_number)
    some_number += 1


#Loop that starts with some_number and ends with 100
for i in range(some_number, 100):
    #prints every number up to 99
    if some_number < 100:
        print("Look at my number:", some_number)
        #adds 1 to our number after each print
        some_number += 1
    else:
        #so the loop finishes when we reah 100
        break



subtractor = 10

for i in range(10, 21, 2):
  some_number -= i
  print(some_number)

#value of subtractor is where our loop starts
subtractor = 10
# the condition < 21 dictates where our loop ends
while subtractor < 21:
    some_number -= subtractor
    #dictates the amount of steps each loop
    subtractor += 2
    print(some_number)
