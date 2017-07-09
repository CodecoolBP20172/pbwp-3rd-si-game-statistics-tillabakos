import csv
from collections import Counter

# Report functions


def count_games(file_name):
    with open(file_name) as in_f:
        text = in_f.read()
    count = Counter(text)
    count_n = count["\n"]
    return count_n


def decide(file_name, year):
    in_list = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
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
        for i in d_items:    
            if i[3] == genre:
                genre_count.append(i[3])
    return len(genre_count)


def get_line_number_by_title(file_name, title):
    in_list = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
    for i in d_items:
        in_list.append(i[0]) 
    for g in in_list:
        if g != title:
            break
        else:
            if g == title:
                g_index = in_list.index(g)
                g_index = g_index + 1
        return g_index

get_line_number_by_title('game_stat.txt', 'The Sims')
