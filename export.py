from reports import count_games

'''

'''
# Export functions


def export_count_games(report_file, filename):
    game_count = count_games(filename)
    with open(report_file, "w") as f:
        f.write(str(game_count))
        return game_count

export_count_games('rep.txt', 'game_stat.txt')




