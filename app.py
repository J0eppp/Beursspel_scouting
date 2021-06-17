import argparse
from random import random

from Game import Game
from Company import Company
from Player import Player

output_file_path = None
game = None


def main():
    global output_file_path
    global game
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action="store", dest="data_file", type=str)
    args = parser.parse_args()
    output_file_path = args.data_file

    # Setup of the game
    game = Game()

    game.state["companies"].append(Company("Frits' Fristi", random() * 100))
    game.state["companies"].append(Company("Bob de bouwer", random() * 100))
    game.state["companies"].append(Company("Bram's Brommers", random() * 100))
    game.state["companies"].append(Company("Mur BV", random() * 100))
    game.state["companies"].append(Company("Bison Burgers", random() * 100))
    game.state["companies"].append(
        Company("Sjoerd's Coffeeshop", random() * 100))

    game.state["players"].append(Player("Player 1", 100))
    game.state["players"].append(Player("Player 2", 100))
    game.state["players"].append(Player("Player 3", 100))
    game.state["players"].append(Player("Player 4", 100))
    game.state["players"].append(Player("Player 5", 100))
    game.state["players"].append(Player("Player 6", 100))
    game.state["players"].append(Player("Player 7", 100))
    game.state["players"].append(Player("Player 8", 100))

    for company in game.state["companies"]:
        print(company.state["name"])

    for player in game.state["players"]:
        print(player.state["name"])

    print("buying a stock")
    print(game.buy_stock(game.state["players"]
          [0], game.state["companies"]
          [0]))

    print(game.state["players"]
          [0].state["capital"])

    print(game.sell_stock(game.state["players"]
          [0], game.state["companies"][0]))

    print(game.state["players"]
          [0].state["capital"])


if __name__ == "__main__":
    main()
