from reports import count_games


# Export functions


def export_count_games(filename='rep.txt'):
    game_count = count_games('game_stat.txt')
    with open(filename, "w") as f:
        f.write(game_count)
