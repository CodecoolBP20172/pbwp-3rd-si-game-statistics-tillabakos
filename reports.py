import csv
from collections import Counter

'''
error handling
  - last row in file has no new line
  - more than 1 empty lines after last line with string
  - empty lines inbetween ?
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
        in_list = []
        for i in d_items[:]:
            in_list.append(int(i[2]))
        for y in in_list:
            if y == year:
                rv = True
                break
            else:
                rv = False
    return rv


def get_latest(file_name):
    title = []
    year = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
        for t in d_items:
            title.append(t[0])
        for y in d_items:
            year.append(int(y[2]))
        t_index = year.index(max(year))
    return(title[t_index])


def count_by_genre(file_name, genre):
    genre_count = []
    game_index = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
        # print(d_items)
        for i in d_items:    
            if i[3] == genre:
                genre_count.append(i[3]) 
        print(genre_count)
    return len(genre_count)