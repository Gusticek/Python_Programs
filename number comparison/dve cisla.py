try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    

    if a>b:
        print(a)
    elif b>a:
        print(b)
    else:
        print("They are the same.")
except ValueError:
    print("Looks like one or both the numbers are not integers.")