import os

folder_path = "D:\\Users\\gugos\\Downloads"

signatures = [
    ("89504E470D0A1A0A", "PNG"),
    ("FFD8FFDB", "JPEG"),
    ("FFD8FFE0", "JPEG"),
    ("25504446", "PDF"),
    ("504B0304", "ZIP"),
    ("526172211A0700", "RAR"),
    ("1F8B08", "GZIP"),
    ("1F9D", "TAR.Z"),
    ("4D546864", "MIDI"),
    ("504B0506", "DOCX"),
    ("54655854", "TXT"),
]

for root, _, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        with open(file_path, 'rb') as f:
            file_start = f.read(32)
        
        file_type = next((ftype for signature, ftype in signatures if file_start.startswith(bytes.fromhex(signature))), "Unknown")
        print(f"File: {file} => Type: {file_type}")