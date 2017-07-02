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


def decide(file_name, year):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
        # print(d_items)
        in_list = []
        for i in d_items:
            in_list = in_list.append(i([2]))
            for y in in_list:
                y == year
    return in_list


decide('game_stat.txt', 1999)
