from reports import *

# Export functions


def export_count_games(report_file, file_name):
    export_count = count_games(file_name)
    with open(report_file, "a") as f:
        f.write(str(export_count) + '\n')
        return export_count


def export_decide(report_file, file_name, year):
    export_decide = decide(file_name, year)
    with open(report_file, "a") as f:
        f.write(str(export_decide) + '\n')
        return export_decide


def export_get_latest(report_file, file_name):
    export_latest = get_latest(file_name)
    with open(report_file, "a") as f:
        f.write(str(export_latest) + '\n')
    return export_latest


def export_count_by_genre(report_file, file_name, genre):
    export_count_by = count_by_genre(file_name, genre)
    with open(report_file, "a") as f:
        f.write(str(export_count_by) + '\n')
    return export_count_by


def export_get_line_number_by_title(report_file, file_name, title):
    export_line_number = get_line_number_by_title(file_name, title)
    with open(report_file, "a") as f:
        f.write(str(export_line_number) + '\n')
    return export_line_number
