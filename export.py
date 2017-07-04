from reports import *

'''

'''
# Export functions


def export_count_games(report_file, filename):
    export_count = count_games(filename)
    with open(report_file, "w") as f:
        f.write(str(export_count) + '\n')
        return export_count


def export_decide(report_file, filename, year):
    export_decide = decide(filename, year)
    with open(report_file, "w") as f:
        f.write(str(export_decide) + '\n')
        return export_decide


def export_get_latest(report_file, filename):
    export_latest = get_latest(filename)
    with open(report_file, "w") as f:
        f.write(str(export_latest) + '\n')
    return export_latest


def export_count_by_genre(report_file, filename, genre):
    export_count_by = count_by_genre(file_name, genre)
    with open(report_file, "w") as f:
        f.write(str(export_count_by) + '\n')
    return export_count_by
