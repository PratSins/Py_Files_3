import csv
print()
data = open('example.csv',encoding='utf-8')
# csv.reader
csv_data = csv.reader(data)
# reformat it into a python object List of Lists
data_lines = list(csv_data)

print("len(data_lines) -- ",len(data_lines))
print()
print("data_lines[0]  -- ",data_lines[0])
print("data_lines[1]  -- ",data_lines[1])
print()
print()

for line in data_lines[:5]:
    print (line)
print()

all_emails = []
for line in data_lines[1:5]:
    all_emails.append(line[3])

print(all_emails)
print()

full_names = []
for line in data_lines[1:5]:
    full_names.append(line[1] + ' ' + line[2])
print(full_names)
print()