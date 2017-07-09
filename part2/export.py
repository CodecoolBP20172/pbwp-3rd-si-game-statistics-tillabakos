from reports import *


# Export functions


def expor_get_most_played(report_file, file_name):
    items = get_most_played(file_name)
    export_reports(items, report_file)
    return items


def export_sum_sold(report_file, file_name):
    items = sum_sold(file_name)
    export_reports(items, report_file)
    return items


def export_get_selling_avg(report_file, file_name):
    items = get_selling_avg(file_name)
    export_reports(items, report_file)
    return items


def export_get_date_avg(report_file, file_name):
    items = get_date_avg(file_name)
    export_reports(items, report_file)
    return items


def export_get_game(report_file, file_name, title):
    items = get_game(file_name, title)
    export_reports(items, report_file)
    return items

# helper function. writes return values to file


def export_reports(items, report_file):
    with open(report_file, "a") as f:
        f.write(str(items) + '\n')
    return items
