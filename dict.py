d = {1:'value', 'key':2, 'hello':[4,7]}
print(d)
print(type(d))

d[3] = 'python'
print(d)
print(d[3])

print('--------------------------------------------------')

students = {"Ben":["Computer Science", "Score:95"], "Curry":["Software Engineering", "Score:91"],
            "James":["Artificial Intelligence", 'Score:89']}

for i in students.items():
    print(i)

print('--------------------------------------------------')

for k in students:
    info = students[k]
    print(k, info)


print('--------------------------------------------------')


points = {x:x ** 2 for x in range(1,6)}
print(points)