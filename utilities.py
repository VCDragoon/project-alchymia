from datetime import datetime
import string


# Returns a string with the current datetime stamp 
# Format generated is: YYYY_MM_DD_HH_MM_SS (24-hour clock)
# Useful in creating unique filenames for logging and other purposes
def timestamp_string() -> str:
    timestamp_str = str(datetime.now()).split(".")[0]
    for i in ["-", ":", " "]:
        timestamp_str = timestamp_str.replace(i, "_")
    print("{}.txt".format(timestamp_str))
    return "{}.txt".format(timestamp_str)



# Takes a string, removes any whitespace, and returns the result
def trim_whitespace(x):
    try:
        x = "".join(x.split())
    except:
        pass
    return x

# Takes a string, removes any punctuation, and returns the result
def remove_punctuation(x):
    exclude = set(string.punctuation)
    try:
        x = ''.join(ch for ch in x if ch not in exclude)
    except:
        pass
    return x
