from reports import count_games
import pprint

# Printing functions


def print_count_games(file_name):
    game_count = count_games(file_name)
    return game_count

print(print_count_games('game_stat.txt'), 'ok')


# def main_print():
