#print("Hello teacher")
#print("Homework №7 Banul")

#1.Написати рекурсивну функцію знаходження ступеня числа.

#def get_num_pow(number, degree):
#     if degree <= 1:
#         return number

#     return number * get_num_pow(number, degree - 1)

#print(get_num_pow(3, 4))
# get_num_pow(3, 4) -> 3 * get_num_pow(3, 3) => 81
# get_num_pow(3, 3) -> 3 * get_num_pow(3, 2) => 27
# get_num_pow(3, 2) -> 3 * get_num_pow(3, 1) => 9
# get_num_pow(3, 1) => 3
################################################

#2.Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.

#def stars(n):

#   return '' if n<=0 else '*'+stars(n-1)

#print(stars(5))
#stars(5) = *****
#stars(4) = (5-1) = ****
#stars(3) = (4-1) = ***
#stars(2) = (3-1) = **
#stars(1) = (2-1) = *
#stars(0) = (n<=0) =
##################################################

#3. Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b
#Користувач вводить a та b. Проілюструйте роботу функції прикладом

def sum_range(a, b):
    if a > b:
        return 0

    return a + sum_range(a+1, b)
#print(sum_range(1, 5))
#sum_range(1,5) = (1+2+3+4+5) = 15
#sum_range(1,4) = (1+2+3+4) = 10
#sum_range(1,3) = (1+2+3) = 6
#sum_range(1,2) = (1+2) = 3