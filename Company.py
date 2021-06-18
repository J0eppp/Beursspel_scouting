from random import random


class Company():
    def __init__(self, name: str, start_value: int, available: int):
        self.state = {
            "name": name,
            "start_value": start_value,
            "value": start_value,
            "available": available,
            "bought": 0,
        }

    def bought(self):
        # Someone bought a stock from this company, save it
        self.state["bought"] += 1

    def sold(self):
        # Someone sold a stock from this company, save it
        self.state["bought"] -= 1

    def next_round(self):
        # Update the value
        new_value = (self.state["value"] * (random() * (2 *
                     self.state["bought"] + 0.5 / self.state["available"]))) * 100
        self.state["value"] = new_value
        self.state["bought"] = 0
        name = self.state["name"]
        print(f"{name} new value: {new_value}")
