path = "example.txt"

separators = {',', ';', '.', ':', '-', '!', '?', '(', ')', '"', "'"}

with open(path, encoding = 'utf-8') as file:
    content = file.read()


for i in separators :
    content = content.replace(i, ' ')

list1 = content.split()

set1 = set()

for i in list1:
    set1.add(i)

print(len(set1))