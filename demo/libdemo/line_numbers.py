# Generates a new file with ln_ prefix for each .py file
# New file contains line numbers of 3 digits with leading zero

import os


def write_line_numbers(dirname, filename):
    targetfilename = dirname + r"\ln_" + filename
    sf = open(dirname + "\\" + filename, "rt")
    tf = open(targetfilename, "wt")
    for lineno, line in enumerate(sf.readlines(), start=1):
        tf.write(f'{lineno:03}: {line}')

    sf.close()
    tf.close()


allfiles = os.walk(r"c:\classroom\apr4\demo\temp")
for (dirname, dirs, files) in allfiles:
    for f in files:
        if f.endswith('.py'):
            write_line_numbers(dirname, f)


