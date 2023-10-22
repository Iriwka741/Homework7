#print("Hello teacher")
#print("Homework №7 Banul")

#1.Написати рекурсивну функцію знаходження ступеня числа.

def get_num_pow(number, degree):
     if degree <= 1:
         return number

     return number * get_num_pow(number, degree - 1)

print(get_num_pow(3, 4))
# get_num_pow(3, 4) -> 3 * get_num_pow(3, 3) => 81
# get_num_pow(3, 3) -> 3 * get_num_pow(3, 2) => 27
# get_num_pow(3, 2) -> 3 * get_num_pow(3, 1) => 9
# get_num_pow(3, 1) => 3