# Positional-only args
def wish(name="Guest", msg="Hello", /):
    print(msg, name)


wish("Jack", "Hi")
wish("Mark")
# wish(name="Jack", msg="Hi")
