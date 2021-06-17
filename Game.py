from Player import Player
from Company import Company
from Stock import Stock


class Game():
    def __init__(self):
        self.state = {
            "companies": [],
            "players": [],
            "history": [],
            "round": 0,
        }

    def start(self):
        if self.state["round"] is not 0:
            return False
        self.state["round"] = 1

        return True

    def buy_stock(self, player: Player, company: Company):
        if not player.state["capital"] >= company.state["value"]:
            return False

        # Create a Stock instance
        stock = Stock(company)

        # Add the stock to the player's stocks and make the player pay
        player.buy_stock(stock)

        # Notify the company that a stock was bought
        company.bought()
        return True

    def sell_stock(self, player: Player, company: Company):
        # Check if the player has this stock
        player_index = self.state["players"].index(player)
        player = self.state["players"][player_index]
        for stock in player.state["stocks"]:
            if stock.state["company"].state["name"] == company.state["name"]:
                # Same company
                # Sell stock
                player.state["capital"] += company.state["value"]
                # Remove stock from player
                player.state["stocks"].remove(stock)

                # Save the player to the game object
                self.state["players"][player_index] = player

                # Notify the company that a stock was sold
                company.sold()
                return True
        return False
