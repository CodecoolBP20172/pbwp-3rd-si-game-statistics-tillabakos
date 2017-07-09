import csv

# Report functions


def get_most_played(file_name):
    game_num = from_filetolist(file_name, 0, 1)
    most_sold = [float(i[1]) for i in game_num]
    game_index = most_sold.index(max(most_sold))
    return game_num[game_index][0]


def sum_sold(file_name):
    total_sold = from_file_singleitem(file_name, 1)
    sales_total = sum(float(i[0]) for i in total_sold)
    return sales_total


def get_selling_avg(file_name):
    total_sold = from_file_singleitem(file_name, 1)
    avg_sales = sum(float(i[0]) for i in total_sold) / len(total_sold)
    return avg_sales


def count_longest_title(file_name):
    title_lenght = from_file_singleitem(file_name, 0)
    maxlen = max(len(i[0]) for i in title_lenght)
    return maxlen


def get_date_avg(file_name):
    release_date = from_file_singleitem(file_name, 2)
    date_avg = sum(int(i[0]) for i in release_date) / len(release_date)
    return round(date_avg)


def get_game(file_name, title):
    in_list = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
    for i in d_items:
        in_list.append(str(i[0])) 
    for g in in_list:
        if g == title:
            g_index = in_list.index(g) 
    g_list = d_items[g_index]
    return g_list


def from_filetolist(file_name, index1, index2):
    line = [[line.split("\t")[index1], line.split("\t")[index2]]
            for line in open(file_name)]
    return line


def from_file_singleitem(file_name, index):
    line = [[line.split("\t")[index]]
            for line in open(file_name)]
    return line


def from_file(file_name):
    all_list = [[line.split("\t")[0:5]]
                for line in open(file_name)]
    return all_list
'''
    new = [[item.replace('\n', '') for item in i] for i in all_list]
    return full_list
'''

print(get_game('game_stat.txt', 'Counter-Strike'))
# print(from_file('game_stat.txt'))
# print(get_date_avg('game_stat.txt'))
# print(from_filetolist('game_stat.txt', 0, 1))