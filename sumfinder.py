import random

target_number = random.randint(50,100)
print ("The target number is: ", target_number)

random_array = [random.randint(1,50) for _ in range(50)]

sorted_array = sorted(random_array)
reversed_array = sorted_array[::-1]

print (random_array)
print (sorted_array)
print (reversed_array)