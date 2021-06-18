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
player_stocks_ax = None
company_ax = None
stocks_ax = None
company_bars = None
player_bars = None
stocks_bars = None


def draw():
    global fig
    global player_ax
    global company_ax
    global stocks_ax
    global game
    global company_bars
    global player_bars
    global stocks_bars
    global player_stocks_bars
    player_names = []
    player_capitals = []
    for player in game.state["players"]:
        player_names.append(player.state["name"])
        player_capitals.append(player.state["capital"])

    for i in range(len(player_bars)):
        player_bars[i].set_height(player_capitals[i])

    players_worth = []
    for i in range(len(game.state["players"])):
        players_worth.append(
            game.state["players"][i].stocks_worth(game.state["companies"]))

    # players_worth = []
    for i in range(len(players_worth)):
        player_stocks_bars[i].set_height(players_worth[i])
        # players_worth.append(
        #     game.state["players"][i].stocks_worth(game.state["companies"]))

    company_values = []
    company_names = []
    for company in game.state["companies"]:
        company_names.append(company.state["name"])
        company_values.append(company.state["value"])

    for i in range(len(company_bars)):
        company_bars[i].set_width(company_values[i])

    company_stocks_percentages = []
    for company in game.state["companies"]:
        company_stocks_percentages.append(
            ((company.state["start_available"] - company.state["available"]) / company.state["start_available"]) * 100)

    for i in range(len(company_stocks_percentages)):
        stocks_bars[i].set_width(company_stocks_percentages[i])

    player_max = max(player_capitals) + 10
    # player_min = min(player_capitals)
    player_min = 0
    player_ax.set_ylim(player_min, player_max)

    players_worth_max = max(players_worth) + 10
    players_worth_min = 0
    player_stocks_ax.set_ylim(players_worth_min, players_worth_max)

    company_max = max(company_values) + 10
    # company_min = min(company_values)
    company_min = 0
    company_ax.set_xlim(company_min, company_max)

    player_ax.plot()
    company_ax.plot()
    fig.canvas.draw()


def main():
    global output_file_path
    global fig
    global player_ax
    global player_stocks_ax
    global company_ax
    global stocks_ax
    global game
    global company_bars
    global player_stocks_bars
    global player_bars
    global stocks_bars
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action="store", dest="data_file", type=str)
    args = parser.parse_args()
    output_file_path = args.data_file

    # Setup of the game
    game = Game()

    game.state["companies"].append(
        Company("Frits'_Fristi", random() * 20, 100))
    game.state["companies"].append(
        Company("Bob_de_bouwer", random() * 20, 100))
    game.state["companies"].append(
        Company("Bram's_Brommers", random() * 20, 100))
    game.state["companies"].append(Company("Mur_BV", random() * 20, 100))
    game.state["companies"].append(
        Company("Bison_Burgers", random() * 20, 100))
    game.state["companies"].append(
        Company("Sjoerd's_Coffeeshop", random() * 100, 100))
    game.state["companies"].append(
        Company("Kut_Ideeën_Inc.", random() * 20, 100))
    game.state["companies"].append(
        Company("Bordspellengebied", random() * 20, 100))
    game.state["companies"].append(Company("Daans_Drank", random() * 20, 100))
    game.state["companies"].append(
        Company("Lucas'_Kinder_Kelder", random() * 20, 100))
    game.state["companies"].append(
        Company("Adolf's_Schilderstore", random() * 20, 100))
    game.state["companies"].append(
        Company("Nordin's_Kapsalon", random() * 20, 100))

    game.state["players"].append(Player("Player1", 100))
    game.state["players"].append(Player("Player2", 100))
    game.state["players"].append(Player("Player3", 100))
    game.state["players"].append(Player("Player4", 100))
    game.state["players"].append(Player("Player5", 100))
    game.state["players"].append(Player("Player6", 100))
    game.state["players"].append(Player("Player7", 100))
    game.state["players"].append(Player("Player8", 100))

    for company in game.state["companies"]:
        print(company.state["name"])

    for player in game.state["players"]:
        print(player.state["name"])

    # Display data
    fig, axs = plt.subplots(2, 2)
    print(axs)
    player_ax = axs[0, 0]
    player_stocks_ax = axs[1, 0]
    company_ax = axs[1, 1]
    stocks_ax = axs[0, 1]
    # player_ax = axs[0]
    # company_ax = axs[1]
    # stocks_ax = axs[2]
    # company_ax = fig.add_subplot(111)

    player_ax.set_title("Kapitaal")
    player_stocks_ax.set_title("Waarde aandelen spelers")
    company_ax.set_title("Waarde bedrijf")
    stocks_ax.set_title("Percentage aandelen verkocht")

    # Display player capital
    player_names = []
    player_capitals = []
    for player in game.state["players"]:
        player_names.append(player.state["name"])
        player_capitals.append(player.state["capital"])

    player_bars = player_ax.bar(player_names, player_capitals, width=0.5)

    players_worth = []
    for i in range(len(game.state["players"])):
        players_worth.append(
            game.state["players"][i].stocks_worth(game.state["companies"]))
    player_stocks_bars = player_stocks_ax.bar(
        player_names, players_worth, width=0.5)

    company_names = []
    company_values = []
    for company in game.state["companies"]:
        company_names.append(company.state["name"])
        company_values.append(company.state["value"])

    company_bars = company_ax.barh(
        company_names, company_values, align="center")

    player_max = max(player_capitals) + 10
    # player_min = min(player_capitals)
    player_min = 0
    player_ax.set_ylim(player_min, player_max)

    players_worth_max = max(players_worth) + 10
    players_worth_min = 0
    player_stocks_ax.set_ylim(players_worth_min, players_worth_max)

    company_max = max(company_values) + 10
    # company_min = min(company_values)
    company_min = 0
    company_ax.set_xlim(company_min, company_max)

    company_stocks_percentages = []
    for company in game.state["companies"]:
        # company_names.append(company.state["name"])
        company_stocks_percentages.append(
            100 - (company.state["start_available"] - company.state["available"] / company.state["start_available"]) * 100)

    stocks_bars = stocks_ax.barh(
        company_names, company_stocks_percentages, align="center")
    stocks_ax.set_xlim(0, 100)

    fig.show()

    # The game begins
    while True:
        command = input("> ")
        if command.startswith("exit"):
            break
        elif command.startswith("buy"):
            cmd = command.split(" ")
            if len(cmd) < 4:
                print("Invalid")
                continue
            p = cmd[1]
            c = cmd[2]
            amt = cmd[3]

            # Check if the player exist
            player_index = None
            for pl_i in range(len(game.state["players"])):
                if game.state["players"][pl_i].state["name"] == p:
                    # player = pl
                    player_index = pl_i

            if player_index == None:
                print("Player was not found")
                continue

            # Check if the company exists
            company_index = None
            for co_i in range(len(game.state["companies"])):
                if game.state["companies"][co_i].state["name"] == c:
                    company_index = co_i

            if company_index == None:
                print("Company was not found")
                continue
            try:
                amount = int(amt)
            except ValueError:
                print("Please enter a valid amount")
                continue

            for _ in range(amount):
                if game.buy_stock(player_index, company_index) == False:
                    print("error buying stock")

        elif command.startswith("sell"):
            cmd = command.split(" ")
            if len(cmd) < 4:
                print("Invalid")
                continue
            p = cmd[1]
            c = cmd[2]
            amt = cmd[3]

            # Check if the player exist
            player_index = None
            for pl_i in range(len(game.state["players"])):
                if game.state["players"][pl_i].state["name"] == p:
                    # player = pl
                    player_index = pl_i

            if player_index == None:
                print("Player was not found")
                continue

            # Check if the company exists
            company_index = None
            for co_i in range(len(game.state["companies"])):
                if game.state["companies"][co_i].state["name"] == c:
                    company_index = co_i

            if company_index == None:
                print("Company was not found")
                continue
            try:
                amount = int(amt)
            except ValueError:
                print("Please enter a valid amount")
                continue

            for _ in range(amount):
                if game.sell_stock(player_index, company_index) == False:
                    print("error selling stock")

        elif command.startswith("next"):
            game.next_round()

        # Update the plt
        draw()


if __name__ == "__main__":
    main()
