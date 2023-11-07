
with open("D:\\Users\\gugos\\Downloads\\spurka.txt", 'rb') as f:
    data = f.read()
    if len(data) < 10:
          print("File is too small to extract 10 bytes.")
    else:
          print(f"First 10 bytes: {data[:10].hex()}")

    if len(data) >= 20:
        print(f"Last 10 bytes: {data[-10:].hex()}")
        
    if len(data) >= 10:
        middle_start = len(data) // 2 - 5
        middle_end = middle_start + 10
        print(f"10 bytes around the middle: {data[middle_start:middle_end].hex()}")
    else:
        print("File is too small to extract 10 bytes around the middle.")
