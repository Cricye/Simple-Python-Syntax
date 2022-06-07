x = 15
y = 2
print('x + y =', x + y)
print('x - y =', x - y)
print('x * y =', x * y)
print('x / y =', x / y)
print('x % y =', x % y)
print('x // y =', x // y)
print('x ** y =', x ** y)

print('x > y is', x > y)
print('x < y is', x < y)
print('x == y is', x == y)
print('x != y is', x != y)
print('x >= y is', x >= y)
print('x <= y is', x <= y)

print(not 0, end=' ')
print(not "", end=' ')
print(not False, end=' ')
print(not True, end=' ')
print(not 2, end=' ')
print(not "Curry")

print(3 or 2, end=' ')
print(0 or 2, end=' ')
print(False or True, end=' ')
print("" or 2)

print(3 and 2, end=' ')
print(0 and 2, end=' ')
print(False and True, end=' ')
print("" and 2)

x = 3
print(x)
print(id(x))

x += 2
print(x)
print(id(x))

print('c' in 'console')
print('j' in 'console')
print('c' not in 'console')
print('j' not in 'console')