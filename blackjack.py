class Player:
    def __init__(self, wallet = 20, name = "player"):
        self.name = name
        self.wallet = wallet

    def __repr__(self):
        return f"This is {self.name} and this player has ${self.wallet} in his wallet"