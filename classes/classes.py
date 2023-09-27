class Deposit:
    def __init__(self, date, description, recipient, amount, currency):
        self.date = date
        self.amount = amount
        self.currency = currency
        self.description = description
        self.recipient = recipient

    def __repr__(self):
        return (f"{self.date} {self.description}\n"
                f"{self.recipient}\n"
                f"{self.amount} {self.currency}")


class Operation(Deposit):
    def __init__(self, date, description, sender, recipient, amount, currency):
        super().__init__(date, description, recipient, amount, currency)
        self.sender = sender

    def __repr__(self):
        return (f"{self.date} {self.description}\n"
                f"{self.sender} -> {self.recipient}\n"
                f"{self.amount} {self.currency}")
