src_data = []
distinct_items = []
results = []

results = [('User Story','All Complete','Num Unique Completed Tasks','Num Unique Incomplete Tasks','Max Completed Task ID')]

def read_src_data():
#function to read data from source file
    with open('doc folder/source_data.csv', 'r') as f:
        next(f)#this is there to skip header
        for line in f:
            words = line.split(',')
            src_data.append((words[0], words[1], words[2].replace("\n","")))
        src_data.sort()# sorting source data
    return src_data

# print(read_src_data())
# print(src_data)

def get_distinct_items():
#function to get a distinct list of items for iteration
    src_data_count = len(src_data)
    for i in range(src_data_count):
        if src_data[i][0] != src_data[i-1][0]: #gets the distinct list as src_data has been sorted
            distinct_items.append(src_data[i][0])
    return(distinct_items)

# print(get_distinct_items())

def data_cleanup():
#main function to analize data and provide output
    src_data_count = len(read_src_data())
    distinct_items_count = len(get_distinct_items())
    for x in range(distinct_items_count):
        max_completed_task_id = 0
        num_unique_completed_tasks =set()
        num_unique_incomplete_tasks =set()
        all_complete    = 'yes'
        for y in range(src_data_count):
            user_story = distinct_items[x]
            if user_story == src_data[y][0]:
                if 'Yes' == src_data[y][2]:#check if item-task is completed, to alocate to correct SET[]
                    num_unique_completed_tasks.add(src_data[y][1])
                else:
                    num_unique_incomplete_tasks.add(src_data[y][1])
                if src_data[y][1] in num_unique_incomplete_tasks:#Remove from complete if found in Incomplete set[]
                    num_unique_completed_tasks.discard(src_data[y][1])
                if max_completed_task_id < int(src_data[y][1]):#Derive the highest task number
                    max_completed_task_id = int(src_data[y][1])
        if len(num_unique_incomplete_tasks) > 0 :#Checks if all tasks in item list is complete
            all_complete    = 'no'
        results.append((user_story,all_complete,str(len(num_unique_completed_tasks)),str(len(num_unique_incomplete_tasks)),str(max_completed_task_id)))

    return(results)


# print(data_cleanup())

def write_out_data():
#function to write data to output file
    data_cleanup()
    out = open('doc folder/output_data.csv','w')
    for i in range(len(results)):
        # output_data =
        # print(output_data)
        out.write(results[i][0] + ',' + results[i][1]+ ',' + results[i][2]+ ',' + results[i][3]+ ',' + results[i][4]+ '\n')
    return()

write_out_data()
