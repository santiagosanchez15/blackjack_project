import random

class Player:
    '''Defaul player class'''
    def __init__(self, name = "player", wallet = 20, wins = 0, loses = 0):
        # Define players attributes
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
    # Get players name
    player1 = Player()
    player1.name = input("Oh, see your name is: ")
    return f"Perfect {player1.name}, Welcome, the BlackJack table is right this way..."

def draw_cards(list_cards):
    '''Draws a random card'''
    return random.choice(list_cards)


def blackjack():
    '''Black Jack Game'''
    total_value = 0
    deck_cards = {"A": [1, 11], 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10}
    list_cards = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    player_first_card = draw_cards(list_cards)
    print(player_first_card)
    player_second_card = draw_cards(list_cards)
    print(player_second_card)
    players_cards = [player_first_card, player_second_card]

    for card in players_cards:
        if card in deck_cards:
            total_value += deck_cards[card]

    return total_value

print(blackjack())

