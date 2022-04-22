def has_upper(s):
    for c in s:
        if c.isupper():
            return True

    return False


def has_digits(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1

    return count
