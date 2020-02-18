from datetime import datetime
import string


def timestamp_string() -> str:
    """
    Returns a string with the current datetime stamp 
    Format generated is: YYYY_MM_DD_HH_MM_SS (24-hour clock)
    Useful in creating unique filenames for logging and other purposes

    """
    timestamp_str = str(datetime.now()).split(".")[0]
    for i in ["-", ":", " "]:
        timestamp_str = timestamp_str.replace(i, "_")
    print("{}.txt".format(timestamp_str))
    return "{}.txt".format(timestamp_str)


def trim_whitespace(x):
    """
    Takes a string, removes any whitespace, and returns the result

    """
    try:
        x = "".join(x.split())
    except:
        pass
    return x

def remove_punctuation(x):
    """
    Takes a string, removes any punctuation, and returns the result

    """
    exclude = set(string.punctuation)
    try:
        x = ''.join(ch for ch in x if ch not in exclude)
    except:
        pass
    return x


def read_csv(csv_path):
    """
    Takes a CSV file, reads it, and returns a dictionary
    Dictionary structure is:
    {header_col1: [row1_item1, row1_item2, ...], header_col2: [row2_item1, row2_item2, ...], ...}
    
    """
    with open(csv_path, 'r') as in_csv:
        header = in_csv.readline().strip().split(',')
        data = {i:[] for i in header}
        for line in in_csv:
            line = line.strip().split(',')
            for i in range(len(line)):
                try: 
                    data[header[i]].append(float(line[i]))
                except ValueError:
                    data[header[i]].append(line[i])
    return data
