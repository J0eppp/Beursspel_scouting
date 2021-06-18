from Player import Player
from Company import Company
from Stock import Stock


class Game():
    def __init__(self):
        self.state = {
            "companies": [],
            "players": [],
            "company_history": [],
            "player_history": [],
            "round": 0,
        }

    def start(self):
        if self.state["round"] is not 0:
            return False
        self.state["round"] = 1

        return True

    def next_round(self):
        # Save everthing to the history arrays
        self.state["company_history"].append(self.state["companies"])
        self.state["player_history"].append(self.state["players"])

        # Next round for the companies (update the price etc)
        for company in self.state["companies"]:
            company.next_round()

        self.state["round"] += 1
        return True

    def buy_stock(self, player: int, company: int):
        if not self.state["players"][player].state["capital"] >= self.state["companies"][company].state["value"]:
            print("not enough money to buy stock")
            return False

        # None were available
        if self.state["companies"][company].state["available"] == 0:
            print("stocks are not available")
            return False

        # Create a Stock instance
        stock = Stock(self.state["companies"][company])

        # Add the stock to the player's stocks and make the player pay
        self.state["players"][player].buy_stock(stock)

        # Notify the company that a stock was bought
        self.state["companies"][company].bought()
        return True

    def sell_stock(self, player: int, company: int):
        # Check if the player has this stock
        for stock in self.state["players"][player].state["stocks"]:
            if stock.state["company"].state["name"] == self.state["companies"][company].state["name"]:
                # Same company
                # Sell stock
                self.state["players"][player].state["capital"] += self.state["companies"][company].state["value"]
                # Remove stock from player
                self.state["players"][player].state["stocks"].remove(stock)

                # Notify the company that a stock was sold
                self.state["companies"][company].sold()
                return True
        print("stock not found")
        return False
