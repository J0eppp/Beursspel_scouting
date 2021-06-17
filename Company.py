class Company():
    def __init__(self, name: str, start_value: int):
        self.state = {
            "name": name,
            "start_value": start_value,
            "value": start_value,
        }

    def bought(self):
        # Someone bought a stock from this company, save it
        pass

    def sold(self):
        # Someone sold a stock from this company, save it
        pass

    def next_round(self):
        # Update the value
        pass
