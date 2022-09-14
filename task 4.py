my_mas=[2, 2, 2, 5, 6, 4, 7, 7, 8, 99, 99]
new_mas=[i for i in my_mas if my_mas.count(i) == 1]

print(new_mas)