My_list=(list(range(20, 240)))
print(My_list)
New_list=[el for el in My_list if ((el % 21) and (el % 20))== 0]
print(New_list)