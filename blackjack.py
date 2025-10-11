class Player:
    '''Defaul player class'''
    def __init__(self, name = "player", wallet = 20, wins = 0, loses = 0):
        self.name = name
        self.wallet = wallet
        self.wins = wins
        self.loses = loses
        

    def __repr__(self):
        return f"This is {self.name} and this player has ${self.wallet} in his wallet.\nThe amount of times {self.name} has won are {self.wins} and the amount of times that {self.name} has lost are {self.loses} times"

def great():
    ''''Great and get name'''
    print("Hello, thank you for coming to Casino Royale")
    print("Before playing, could I check your ID")
    player1 = Player()
    player1.name = input("Oh, see your name is: ")
    return f"Perfect {player1.name}, Welcome, the BlackJack table is right this way..."

print(great())

