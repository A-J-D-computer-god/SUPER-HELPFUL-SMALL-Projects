try:

 import random

 num = int(input("Hi we hope you had great times... please add the number"))

 numbers = random.sample(range(1,num+1),num)
 print(numbers)

 f = open("Random numbers.txt","w")
 f . write(numbers)
 f . close()

except: print("Err... We were dragged into a black hole... Retry...")