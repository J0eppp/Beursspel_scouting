from Stock import Stock


class Player():
    def __init__(self, name: str, capital: int):
        self.state = {
            "name": name,
            "capital": capital,
            "stocks": [],
        }

    def stocks_worth(self, companies):
        worth = 0
        for stock in self.state["stocks"]:
            for company in companies:
                if company.state["name"] == stock.state["company"].state["name"]:
                    # Found company
                    worth += stock.state["company"].state["value"]
        return worth

    def buy_stock(self, stock: Stock):
        self.state["stocks"].append(stock)
        self.state["capital"] -= stock.state["bought_at"]

    def add_stock(self, stock: Stock):
        self.state["stocks"].append(stock)
