import argparse
import json
import os
import random
import matplotlib.pyplot as plt
import numpy as np


data = {
    "bedrijven": {
        "Frits' Fristi": {},
        "Bob de bouwer": {},
        "Bram's brommers": {},
        "Mur BV": {},
        "Bison Burgers": {},
        "Sjoerd's Coffeeshop": {},
    },
    "current_round": 0,
    "history": [],
    "players": {
        "Speler 1": {}
    }
}

file = None


def save_data(path):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def next_round():
    global data
    current_round = data["current_round"]
    next_round = current_round + 1
    # Save the current round into history
    data["history"].append(data["bedrijven"])

    # This needs to be updated
    for name in data["bedrijven"]:
        new_value = random.random() * 100
        data["bedrijven"][name]["value"] = new_value

    data["current_round"] = next_round


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", action="store", dest="data_file", type=str)
    args = parser.parse_args()

    global data
    global file

    if args.data_file is not None:
        if os.path.isfile(args.data_file) == True:
            file = open(args.data_file)
            file.read()  # I have no clue why this is needed, but DO NOT REMOVE THIS
            if len(file.read()) > 0:
                content = file.read()
                data = json.loads(content)

    for name in data["bedrijven"]:
        start_value = random.random() * 100
        data["bedrijven"][name]["start_value"] = start_value
        data["bedrijven"][name]["value"] = start_value

    next_round()
    next_round()
    next_round()

    print(data["history"][2]["Bob de bouwer"]["value"])
    print(data["history"][2]["Bob de bouwer"]["start_value"])
    print(data["bedrijven"]["Bob de bouwer"]["value"])

    # Display company values
    fig, axs = plt.subplots(1)
    fig.suptitle("Waarde bedrijven")
    y = {
        "Frits' Fristi": [],
        "Bob de bouwer": [],
        "Bram's brommers": [],
        "Mur BV": [],
        "Bison Burgers": [],
        "Sjoerd's Coffeeshop": [],
    }
    for round in data["history"]:
        for company in round:
            # print(round[company]["value"])
            y[company].append(round[company]["value"])

    for company in y:
        axs.plot(np.array(y[company]))
        print(np.array(y[company]))

    fig.show()
    plt.show()

    save_data(args.data_file)


if __name__ == "__main__":
    main()
