from sys import argv

script_name, num_1,num_2,num_3 = argv

print("имя скрипта", script_name)
print("размер выработки в часах:", num_1)
print("размер ставки в час:", num_2)
print("размер премии:", num_3)

def salary(num_1, num_2, num_3):
    return(int(num_1)*int(num_2)) + int(num_3)

print(salary(num_1, num_2, num_3))