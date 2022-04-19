src_data = []

with open('doc folder/source_data.csv', 'r') as f:
    next(f)
    for line in f:
            words = line.split(',')
            src_data.append((words[0], words[1], words[2].replace("\n","")))
    src_data.sort()

print(src_data)
