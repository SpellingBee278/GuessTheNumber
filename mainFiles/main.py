from random import randint
import numpy as np

nums = randint(0, 100)
print("I am thinking of a number between 1 and 100")
inp = input("What number am I thinking of?")
even_nums = [0, 2, 4, 6, 8, 10,

             12, 14, 16, 18, 20,

             22, 24, 26, 28, 30,

             32, 34, 36, 38, 40,

             42, 44, 46, 48, 50,

             52, 54, 56, 58, 60,

             62, 64, 66, 68, 70,

             72, 74, 76, 78, 80,

             82, 84, 86, 88, 90,

             92, 94, 96, 98, 100]
if nums == even_nums:
    print("My number is even")

else:
    print("My number is odd.")
