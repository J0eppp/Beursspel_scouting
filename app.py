import argparse
from random import random
import matplotlib.pyplot as plt
import numpy as np
import math

from Game import Game
from Company import Company
from Player import Player

output_file_path = None
game = None

fig = None
player_ax = None
company_ax = None
company_bars = None
player_bars = []


def draw():
    global fig
    global player_ax
    global company_ax
    global game
    global company_bars
    global player_bars
    player_names = []
    player_capitals = []
    for player in game.state["players"]:
        player_names.append(player.state["name"])
        player_capitals.append(player.state["capital"])

    for i in range(len(player_bars)):
        player_bars[i].set_height(player_capitals[i])

    company_values = []
    company_names = []
    for company in game.state["companies"]:
        company_names.append(company.state["name"])
        company_values.append(company.state["value"])

    for i in range(len(company_bars)):
        company_bars[i].set_height(company_values[i])

        # plt.autoscale()

    player_max = max(player_capitals) + 10
    # player_min = min(player_capitals)
    player_min = 0
    player_ax.set_ylim(player_min, player_max)

    company_max = max(company_values) + 10
    # company_min = min(company_values)
    company_min = 0
    company_ax.set_ylim(company_min, company_max)

    player_ax.plot()
    company_ax.plot()
    fig.canvas.draw()


def main():
    global output_file_path
    global fig
    global player_ax
    global company_ax
    global game
    global company_bars
    global player_bars
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action="store", dest="data_file", type=str)
    args = parser.parse_args()
    output_file_path = args.data_file

    # Setup of the game
    game = Game()

    game.state["companies"].append(Company("Frits' Fristi", random() * 20, 20))
    game.state["companies"].append(Company("Bob de bouwer", random() * 20, 20))
    game.state["companies"].append(
        Company("Bram's Brommers", random() * 20, 20))
    game.state["companies"].append(Company("Mur BV", random() * 20, 20))
    game.state["companies"].append(Company("Bison Burgers", random() * 20, 20))
    game.state["companies"].append(
        Company("Sjoerd's Coffeeshop", random() * 100, 20))
    game.state["companies"].append(
        Company("Kut Ideeën Inc.", random() * 20, 20))
    game.state["companies"].append(
        Company("Bordspellengebied", random() * 20, 20))
    game.state["companies"].append(Company("Daans Drank", random() * 20, 20))
    game.state["companies"].append(
        Company("Lucas' Kinder Kelder", random() * 20, 20))
    game.state["companies"].append(
        Company("Adolf's Schilderstore", random() * 20, 20))
    game.state["companies"].append(
        Company("Nordin's Kapsalon", random() * 20, 20))

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

    # print("buying a stock")
    print(game.buy_stock(game.state["players"]
          [0], game.state["companies"]
          [0]))

    # print(game.state["players"]
    #       [0].state["capital"])

    # print(game.sell_stock(game.state["players"]
    #       [0], game.state["companies"][0]))

    # print(game.state["players"]
    #       [0].state["capital"])

    # Display data
    plt.autoscale()

    fig, axs = plt.subplots(2)
    player_ax = axs[0]
    company_ax = axs[1]
    # company_ax = fig.add_subplot(111)

    # Display player capital
    player_names = []
    player_capitals = []
    for player in game.state["players"]:
        player_names.append(player.state["name"])
        player_capitals.append(player.state["capital"])

    player_bars = player_ax.bar(player_names, player_capitals)
    # fig.show()

    company_names = []
    company_values = []
    for company in game.state["companies"]:
        company_names.append(company.state["name"])
        company_values.append(company.state["value"])

    company_bars = company_ax.bar(company_names, company_values)

    player_max = max(player_capitals) + 10
    # player_min = min(player_capitals)
    player_min = 0
    player_ax.set_ylim(player_min, player_max)

    company_max = max(company_values) + 10
    # company_min = min(company_values)
    company_min = 0
    company_ax.set_ylim(company_min, company_max)

    fig.show()

    # plt.show()

    # The game begins
    while True:
        command = input("> ")
        if command.startswith("exit"):
            break
        elif command.startswith("next"):
            game.next_round()

        # Update the plt
        draw()
        # player_capitals = []
        # for player in game.state["players"]:
        #     player_names.append(player.state["name"])
        #     player_capitals.append(player.state["capital"])

        # for i in range(len(player_bars)):
        #     player_bars[i].set_height(player_capitals[i])

        # company_values = []
        # for company in game.state["companies"]:
        #     company_names.append(company.state["name"])
        #     company_values.append(company.state["value"])

        # for i in range(len(company_bars)):
        #     company_bars[i].set_height(company_values[i])

        # # plt.autoscale()

        # player_ax.plot()
        # company_ax.plot()
        # fig.canvas.draw()


if __name__ == "__main__":
    main()
