def wish(msg, name):
    print(msg, name)


wish("Hi", "Tom")  # Positional
wish(name="Scott", msg="Hello")  # Keyword args
wish(msg="Good Morning", name="Richards")

print(10, 20, sep="-")
