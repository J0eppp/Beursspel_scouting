from Company import Company


class Stock():
    def __init__(self, company: Company):
        self.state = {
            "company": company,
            "bought_at": company.state["value"],
        }
