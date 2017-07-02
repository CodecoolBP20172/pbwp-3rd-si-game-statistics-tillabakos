from reports import count_games
import pprint

# Printing functions


def print_count_games():
    game_count = count_games('game_stat.txt')
    print(game_count)
