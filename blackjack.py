import random

class Player:
    '''Defaul player class'''
    def __init__(self, name = "player", wallet = 20, wins = 0, loses = 0, cards = None):
        ''' Define players attributes'''
        self.name = name
        self.wallet = wallet
        self.wins = wins
        self.loses = loses
        self.cards = cards if cards is not None else []
        

    def __repr__(self):
        return f"This is {self.name} and this player has ${self.wallet} in his wallet.\nThe amount of times {self.name} has won are {self.wins} and the amount of times that {self.name} has lost are {self.loses} times"

class House:
    '''Class House menaing casino'''
    def __init__(self, name = "The House", wins = 0, loses = 0, cards = None):
        '''Define House attributes'''
        self.name = name
        self.wins = wins
        self.loses = loses
        self.cards = cards if cards is not None else []

    def __repr__(self):
        '''House description'''
        return f"This is {self.name}, the casino itself, it has {self.wins} wins and {self.loses} loses, be careful"

def great():
    ''''Great and get name'''
    print("Hello, thank you for coming to Casino Royale")
    print("Before playing, could I check your ID")
    # Get players name
    player1 = Player()
    player1.name = input("Oh, see your name is: ")
    print(f"Perfect {player1.name}, Welcome, the BlackJack table is right this way...")
    return 0

def draw_cards():
    '''Draws a random card'''
    list_cards = ["A", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    return random.choice(list_cards)

def Ace_checker():
    '''Check if player wnat 1 or 11'''
    A_input = int(input("Do you want your Ace to be 1 or 11: "))
    # Check user input
    while A_input != 1 and A_input != 11:
        A_input = input("Do you want your Ace to be 1 or 11: ")
    return A_input

def Ace_house_checker(total_value):
    if total_value <= 10:
        return 11
    else:
        return 1        

def house_count(house):
    '''Count total cards of player'''
    # Create accumulator, set value of cards
    total_value = 0
    deck_cards = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10, 11: 11}
    for card in house.cards:
        if card == "A":
                card = Ace_house_checker(total_value)
                total_value += deck_cards[card]
        elif card in deck_cards:
            total_value += deck_cards[card]
    return total_value


def player_count(player):
    '''Count total cards of player'''
    # Create accumulator, set value of cards
    total_value = 0
    deck_cards = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10, 11: 11}
    for card in player.cards:
        if card == "A":
                card = Ace_checker()
                total_value += deck_cards[card]
        elif card in deck_cards:
            total_value += deck_cards[card]
    return total_value


def players_game(player):
    '''Black Jack Game'''
    # First movement
    player_first_card = draw_cards()
    player_second_card = draw_cards()
    print(f"Oh you got a {player_first_card} and a {player_second_card}")
    player.cards = [player_first_card, player_second_card]

    return player_count(player)
    
def house_dealer_game(house):
    '''Retyrn the house cards'''
    # Set basic actions
    house_first_card = draw_cards()
    house_second_card = draw_cards()
    print(f"Oh the house got a {house_first_card} and a {house_second_card}")
    house.cards = [house_first_card, house_second_card]

    return house_count(house)
    

def blackjack_player(player):
    '''Handles, secodn round for player'''
    if player.total > 21:
        return f"You have {player.total} you lost"

    user_input = input(f"Your total is: {player.total}, Do you want another card? ")

    while user_input.upper() not in ["YES", 'NO']:
        user_input = input("Please only Yes or No. Do you want another card? ")
    
    if user_input.upper() == "YES":
        player_new_card = draw_cards()
        print(f"You drew a {player_new_card}")
        player.total += player_count(player_new_card)
            
        return blackjack_player(player)

    elif user_input.upper() == "NO":
        return f"You have {player.total}"


def blackjack_dealer(house):
    '''Handles, second round for dealer'''

    if house.total > 21:
        return f"The dealer has {house.total}, the house lost!"
    
    elif house.total < 17:
        dealer_draw = draw_cards()
        print(f"THe house drew a {dealer_draw}")
        house.total += house_count(dealer_draw)

        return blackjack_dealer(house)
    
    else: 
        return house.total

