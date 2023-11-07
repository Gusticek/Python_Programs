with open("D:\\Users\\gugos\\Downloads\\spurka.txt", 'rb') as f:
    while (chunk := f.read(16)):
        hex_data = " ".join(f"{byte:02X}" for byte in chunk)
        print(hex_data)