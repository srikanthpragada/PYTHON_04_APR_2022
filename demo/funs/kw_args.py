def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def showall(*args, **kwargs):
    print(args)
    for k, v in kwargs.items():
        print(k, v)


show(a=10, b=20, c=20, msg="Hello")
showall(10, 20, 30, x=1, y=20)
