def add(n1, n2):
    return n1 + n2


def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(add(10, 20))
print(count_upper("AbcXyz"))
