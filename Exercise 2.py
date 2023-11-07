byte_value = int(input("Enter the byte value (0-255): "))

if not (0 <= byte_value <= 255):
    print("Invalid byte value. Please enter an integer between 0 and 255.")
else:
    with open("D:\\Users\\gugos\\Downloads\\spurka.txt", 'rb') as file:
        content = file.read()
        occurrences = content.count(byte_value)
        print(f"The byte: {byte_value} is in the file: {occurrences} times")


