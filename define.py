def curry():
    print('Stephen Curry')
    print('30')
    print('NBA')

curry()



def pow(x,n):
    ret = 1
    for i in range(n):
        ret *= x
    return ret

print(pow(2,4))
print(pow(5,2))


def pow(x,n=2):
    ret = 1
    for i in range(n):
        ret *= x
    return ret

print(pow(3.5))