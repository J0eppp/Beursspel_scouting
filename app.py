import argparse
from random import random
import matplotlib.pyplot as plt

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

history_companies_ax = None
history_players_ax = None

company_bars = None
player_bars = None
stocks_bars = None
player_stocks_bars = None

history_companies_lines = None
history_players_lines = None


def draw():
    global fig
    global player_ax
    global company_ax
    global stocks_ax
    global history_companies_ax
    global history_players_ax
    global game
    global company_bars
    global player_bars
    global stocks_bars
    global player_stocks_bars
    global history_companies_lines
    global history_players_lines
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
    player_min = 0
    player_ax.set_ylim(player_min, player_max)

    players_worth_max = max(players_worth) + 10
    players_worth_min = 0
    player_stocks_ax.set_ylim(players_worth_min, players_worth_max)

    company_max = max(company_values) + 10
    company_min = 0
    company_ax.set_xlim(company_min, company_max)

    fig.canvas.draw()


def draw_next_round():
    global fig
    global history_companies_ax
    global history_players_ax
    global game
    global history_companies_lines
    global history_players_lines

    player_names = []
    for player in game.state["players"]:
        player_names.append(player.state["name"])

    company_names = []
    for company in game.state["companies"]:
        company_names.append(company.state["name"])

    if game.state["round"] > 0:
        player_history = []
        player_history_x = list(
            range(1, len(game.state["player_history"]) + 1))
        for _ in game.state["player_history"][0]:
            player_history.append([])

        for player_i in range(len(player_history)):
            for round_i in range(len(game.state["player_history"])):
                # print("Player: " + str(player_i) + " round: " + str(round_i) + " -> " + str(game.state["player_history"][round_i][player_i].worth(
                # game.state["company_history"][round_i])))
                player_history[player_i].append(game.state["player_history"][round_i][player_i].worth(
                    game.state["company_history"][round_i]))

        history_players_ax.clear()
        history_companies_ax.clear()

        for i in range(len(player_history)):
            player = player_history[i]
            # print("Player: " + str(player))
            name = player_names[i]
            line = history_players_ax.plot(
                player_history_x, player, label=name)

        history_players_ax.legend()

        company_history = []
        company_history_x = list(
            range(1, len(game.state["company_history"]) + 1))
        for _ in game.state["company_history"][0]:
            company_history.append([])

        for company_i in range(len(company_history)):
            for round_i in range(len(game.state["company_history"])):
                company_history[company_i].append(
                    game.state["company_history"][round_i][company_i].state["value"])

        for i in range(len(company_history)):
            company = company_history[i]
            name = company_names[i]
            history_companies_ax.plot(company_history_x, company, label=name)

        history_companies_ax.legend()

        history_players_ax.set_xlabel("Ronde")
        history_players_ax.set_ylabel("Euro")

        history_companies_ax.set_xlabel("Ronde")
        history_companies_ax.set_ylabel("Euro")

    fig.canvas.draw()


def main():
    global output_file_path
    global fig
    global player_ax
    global player_stocks_ax
    global company_ax
    global stocks_ax
    global history_companies_ax
    global history_players_ax
    global game
    global company_bars
    global player_stocks_bars
    global player_bars
    global stocks_bars
    global history_companies_lines
    global history_players_lines

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

    # Display data
    fig, axs = plt.subplots(2, 3)
    player_ax = axs[0, 0]
    player_stocks_ax = axs[1, 0]
    company_ax = axs[1, 1]
    stocks_ax = axs[0, 1]
    history_companies_ax = axs[0, 2]
    history_players_ax = axs[1, 2]

    player_ax.set_title("Kapitaal")
    player_stocks_ax.set_title("Waarde aandelen spelers")
    company_ax.set_title("Waarde bedrijf")
    stocks_ax.set_title("Percentage aandelen verkocht")
    history_players_ax.set_title("Geschiedenis waarde speler")
    history_companies_ax.set_title("Geschiedenis waarde bedrijven")

    history_players_ax.set_xlabel("Ronde")
    history_players_ax.set_ylabel("Euro")

    history_companies_ax.set_xlabel("Ronde")
    history_companies_ax.set_ylabel("Euro")

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
    player_min = 0
    player_ax.set_ylim(player_min, player_max)

    players_worth_max = max(players_worth) + 10
    players_worth_min = 0
    player_stocks_ax.set_ylim(players_worth_min, players_worth_max)

    company_max = max(company_values) + 10
    company_min = 0
    company_ax.set_xlim(company_min, company_max)

    company_stocks_percentages = []
    for company in game.state["companies"]:
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

        elif command.startswith("infoc"):
            cmd = command.split(" ")
            if len(cmd) < 2:
                print("Please enter a company's name")
                continue
            name = cmd[1]
            for company in game.state["companies"]:
                if company.state["name"] == name:
                    worth = company.state["value"]
                    print(f"De waarde van {name} is €{worth}")
                    available = company.state["available"]
                    print(f"{name} heeft {available} aandelen beschikbaar")

        elif command.startswith("infop"):
            cmd = command.split(" ")
            if len(cmd) < 2:
                print("Please enter a player's name")
                continue

            name = cmd[1]
            for player in game.state["players"]:
                if player.state["name"] == name:
                    capital = player.state["capital"]
                    stocks = {
                        "Frits'_Fristi": 0,
                        "Bob_de_bouwer": 0,
                        "Bram's_Brommers": 0,
                        "Mur_BV": 0,
                        "Bison_Burgers": 0,
                        "Sjoerd's_Coffeeshop": 0,
                        "Kut_Ideeën_Inc.": 0,
                        "Bordspellengebied": 0,
                        "Daans_Drank": 0,
                        "Lucas'_Kinder_Kelder": 0,
                        "Adolf's_Schilderstore": 0,
                        "Nordin's_Kapsalon": 0,
                    }
                    companies = {
                        "Frits'_Fristi": 0,
                        "Bob_de_bouwer": 0,
                        "Bram's_Brommers": 0,
                        "Mur_BV": 0,
                        "Bison_Burgers": 0,
                        "Sjoerd's_Coffeeshop": 0,
                        "Kut_Ideeën_Inc.": 0,
                        "Bordspellengebied": 0,
                        "Daans_Drank": 0,
                        "Lucas'_Kinder_Kelder": 0,
                        "Adolf's_Schilderstore": 0,
                        "Nordin's_Kapsalon": 0,
                    }
                    for stock in player.state["stocks"]:
                        # if stocks.get[stock.state["company"].state["name"]] == None:
                        #     stocks[stock.state["company"].state["name"]] = 1
                        #     companies[stock.state["company"].state["name"]
                        #               ] = stock.state["company"].state["value"]
                        # else:
                        stocks[stock.state["company"].state["name"]] += 1
                        companies[stock.state["company"].state["name"]
                                  ] = stock.state["company"].state["value"]

                    print(f"Naam: {name}")
                    print(f"Kapitaal: {capital}")
                    for company in stocks:
                        total_value = stocks[company] * companies[company]
                        print(
                            f"Je hebt {stocks[company]} van {company}, dat is €{total_value}")
                    print(stocks)

        elif command.startswith("next"):
            game.next_round()
            draw_next_round()

        # Update the plt
        draw()


if __name__ == "__main__":
    main()
