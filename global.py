global_x = 6
def f():
    x = 3
    global_x = 5
    print(x, global_x)

f()
print(global_x)

print('----------------------------------------------------------------')

global_x = 6
def f():
    x = 3
    global global_x
    global_x = 5
    print(x, global_x)

f()
print(global_x)


print('----------------------------------------------------------------')

global_x = 6
a = [1,2,3]
def f(y,z):
    x = 3
    y = 5
    z[0] = 10
    print(y)
    print(z)

f(global_x, a)
print(global_x)
print(a)