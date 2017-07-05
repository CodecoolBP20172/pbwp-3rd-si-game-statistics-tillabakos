import csv

# Report functions


def get_most_played(file_name):
    title = []
    sales_num = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
        for t in d_items:
            title.append(t[0])
        for y in d_items:
            sales_num.append(float(y[1]))
        t_index = sales_num.index(max(sales_num))
    return(title[t_index])


def sum_sold(file_name):
    sales = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
        for s in d_items:
            sales.append(float(s[1]))
        sales_total = sum(sales)
    return sales_total


def get_selling_avg(file_name):
    sales = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
        for s in d_items:
            sales.append(float(s[1]))
        avgSales = sum(sales) / len(sales)
        print(avgSales)
    return avgSales


def count_longest_title(file_name):
    longest = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
        for i in d_items:
            longest.append(i[0])
        maxlen = max(len(i) for i in longest)
    return maxlen


def get_date_avg(file_name):
    year_avg = []
    with open(file_name) as f:
        reader = csv.reader(f, delimiter="\t")
        d_items = list(reader)
        for s in d_items:
            year_avg.append(int(s[2]))
        avg_ofYears = sum(year_avg) / len(year_avg)
    return round(avg_ofYears)


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
            g_index = g_index
    return d_items[g_index]

print(get_game('game_stat.txt', 'Counter-Strike'))

