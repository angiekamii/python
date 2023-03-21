# local variable

def car():
    x = "volvo"
    print(x)


car()

# global variable
y = "phone"


def device():
    global y
    print(y)


device()
