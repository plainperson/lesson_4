from functools import reduce

my_list=list(range(100, 1000))
print(my_list)
my_list2=[el for el in my_list if el % 2 ==0]
print(my_list2)

def my_func(prev_el, el):
    return prev_el * el

print (reduce(my_func,(my_list2)))