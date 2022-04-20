src_data = []
distinct_items = []


def read_src_data():
    with open('doc folder/source_data.csv', 'r') as f:
        next(f)
        for line in f:
            words = line.split(',')
            src_data.append((words[0], words[1], words[2].replace("\n","")))
        src_data.sort()
    return src_data

print(read_src_data())

def get_distinct_items():
    src_data_count = len(src_data)
    for i in range(src_data_count):
        if src_data[i][0] != src_data[i-1][0]:
            distinct_items.append(src_data[i][0])
    return(distinct_items)
print(get_distinct_items())
