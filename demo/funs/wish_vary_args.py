def wish(*names, msg="Hello"):
    for n in names:
        print(msg, n)


wish("Tom", "Jack")
wish("Bob", "Joe", msg="Hi")
