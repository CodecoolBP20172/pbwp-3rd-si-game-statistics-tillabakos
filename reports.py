from collections import Counter

'''
error handling
  - last row in file has no new line
  - more than 1 empty lines after last line with string 
'''

# Report functions


def count_games(file_name):
    with open(file_name) as in_f:
        text = in_f.read()
    count = Counter(text)
    count_n = count["\n"]
    return count_n


