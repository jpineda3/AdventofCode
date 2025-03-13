# Function to read a file and return a list of lines removing the newline character
def read_file(file):
    with open(file) as f:
        return f.read().splitlines()
    
def strlist_to_intlist(lst, delimiter=None):
    intlist = [] * len(lst)
    for line in lst:
        if delimiter:
            line_list = line.split(delimiter)
        else:
            line_list = line.split()  # Split by any whitespace and discard empty strings
        intlist.append([int(x) for x in line_list])  # Convert each element to an integer
    return intlist
        
def get_columns(lst):
    num_columns = len(lst[0])
    columns = [] * num_columns
    for i in range(num_columns):
        columns.append([sublist[i] for sublist in lst])
    return columns

def count_occurances(lst, item):
    count = 0
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count