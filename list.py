a = [1,2,3]
print(a)
print(type(a))

my_list = [2, 3.14, ['Curry', 'James', '30 23'], 'Python Lang']
print(my_list)
print(my_list[2])

my_list[-3] = 8.9
print(my_list)

print(my_list[0:4:2])
print(my_list[2:])

print(id(my_list))

print('--------------------------------------------------')
for e in my_list:
    print(e)
print('--------------------------------------------------')
alist = [1,2,3,4,5]
alist = [x ** 2 for x in alist if x % 2 == 0]
print(alist)
print('--------------------------------------------------')
alist = [x ** 2 for x in range(6)]
print(alist)