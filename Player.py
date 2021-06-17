from Stock import Stock


class Player():
    def __init__(self, name: str, capital: int):
        self.state = {
            "name": name,
            "capital": capital,
            "stocks": [],
        }

    def buy_stock(self, stock: Stock):
        self.state["stocks"].append(stock)
        self.state["capital"] -= stock.state["bought_at"]

    def add_stock(self, stock: Stock):
        self.state["stocks"].append(stock)
