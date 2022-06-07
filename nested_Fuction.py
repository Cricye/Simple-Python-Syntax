def print_msg(msg):
    def printer():
        print(msg)
    return printer()

print_msg('Curry')