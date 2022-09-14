my_list=[6, 7, 3 ,5, 9, 0, 12, 15]
my_list_2=[]
for i in range (len(my_list)):
    if my_list[i] > my_list[i-1]:
        my_list_2.append(my_list[i])

print(my_list_2)