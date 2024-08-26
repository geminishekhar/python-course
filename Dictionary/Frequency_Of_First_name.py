names = ["John Smith", "Jane Doe", "John Doe", "Alice Johnson", "Jane Smith", "Alice Brown","Nur Chauwdhary","Bright "]
frequency_map = {}

for x in names:
    split_String=x.split()
    first_name=split_String[0]
    if first_name in frequency_map:
        frequency_map[first_name]=frequency_map[first_name]+1
    else:
        frequency_map[first_name]=1

print(frequency_map)
