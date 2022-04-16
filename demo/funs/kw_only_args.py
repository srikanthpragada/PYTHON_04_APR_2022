# Keyword-only args
def wish(*, msg="Hello", name="Guest"):
    print(msg, name)


#wish("Jack", "Hi")
wish(name="Jack", msg="Hi")
