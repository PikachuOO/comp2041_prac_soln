d = {}
name = input("Enter student name: ")
fine = int(input("Enter library fine: "))

while True:

    if name not in d:
        d[name] = 0
    d[name] += fine

    # we try to take in input, if we get a EOF, (Ctrl-D)
    # we print a newline and end the loop
    try:
        name = input("Enter student name: ")
        fine = int(input("Enter library fine: "))
    except EOFError:
        print()
        break

print("Expel {} whose library fines total ${}".format(
    #get the max name based on value
    max(d, key = lambda x: d[x]),
    #get the max value
    max(d.values())))
