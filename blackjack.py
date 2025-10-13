import random

class Player:
    '''Defaul player class'''
    def __init__(self, name = "player", wallet = 20, wins = 0, loses = 0, cards = None, total = 0):
        ''' Define players attributes'''
        self.name = name
        self.wallet = wallet
        self.wins = wins
        self.loses = loses
        self.cards = cards if cards is not None else []
        self.total = total
        

    def __repr__(self):
        return f"This is {self.name} and this player has ${self.wallet} in his wallet.\nThe amount of times {self.name} has won are {self.wins} and the amount of times that {self.name} has lost are {self.loses} times"

    def bet(self, house):
        '''Method to make the user bet'''
        print(f"You have ${self.wallet}")
        user_bet = float(input("How much do you want to bet on blackjack: "))
        if user_bet > self.wallet:
            print("You Dont have enough money")
            return self.bet(house)
        elif self.wallet == 0:
            return 1

        results = blackjack(self, house)
        if results == True:
            self.wallet += user_bet * 2
            print(f"You made ${user_bet * 2}")
            return 0
        if results == 0:
            print("Its a draw, no one wins")
            return 0
        else:
            self.wallet = self.wallet - user_bet
            return f"You lost ${user_bet}"

class House:
    '''Class House menaing casino'''
    def __init__(self, name = "The House", wins = 0, loses = 0, cards = None, total = 0):
        '''Define House attributes'''
        self.name = name
        self.wins = wins
        self.loses = loses
        self.cards = cards if cards is not None else []
        self.total = total

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
    return player1

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
    player.total = 0
    player_first_card = draw_cards()
    player_second_card = draw_cards()
    print(f"Oh you got a {player_first_card} and a {player_second_card}")
    player.cards = [player_first_card, player_second_card]
    total = player_count(player)
    print(f"Your total is {total}")

    return total
    
def house_dealer_game(house):
    '''Retyrn the house cards'''
    # Set basic actions
    house.total = 0
    house_first_card = draw_cards()
    house_second_card = draw_cards()
    print(f"Oh the house got a {house_first_card} and a {house_second_card}")
    house.cards = [house_first_card, house_second_card]
    total = house_count(house)
    print(f"The house total is {total}")

    return total
    

def blackjack_player(player):
    '''Handles, secodn round for player'''
    if player.total > 21:
        return player.total

    user_input = input(f"Your total is {player.total}. Do you want another card? ")

    # Check valid user input
    while user_input.upper() not in ["YES", 'NO']:
        user_input = input("Please only Yes or No. Do you want another card? ")
    
    # get more cards
    if user_input.upper() == "YES":
        player.new_card = draw_cards()
        print(f"You drew a {player.new_card}")
        player.cards.append(player.new_card)
        player.total = player_count(player)

        return blackjack_player(player)

    # return the total value
    elif user_input.upper() == "NO":
        return player.total


def blackjack_dealer(house):
    '''Handles, second round for dealer'''

    print(f"The house total is {house.total}")
    # Check house is no more than 21
    if house.total > 21:
        return house.total
    
    
    # if less than 17 keep going
    elif house.total < 17:
        house.new_draw = draw_cards()
        print(f"The house drew a {house.new_draw}")
        house.cards.append(house.new_draw)
        house.total = house_count(house)

        # Recursion to eithe get another card or return
        return blackjack_dealer(house)
    
    else: 
        return house.total

def blackjack(player1, casino):
    '''returns wether the player won or lost'''

    # Chck first round of blackjack
    player1.total = players_game(player1)
    casino.total = house_dealer_game(casino)

    # Checks second round of blackjack
    player1.total = blackjack_player(player1)
    casino.total = blackjack_dealer(casino)

    # Chceck all possible outocmes
    if player1.total > 21:
        print("Sorry you lost")
        return False 
    
    elif player1.total > 21 and casino.total > 21:
        return 0
    
    elif player1.total == casino.total:
        return 0

    elif player1.total > casino.total or casino.total > 21:
        print("You won")
        return True
    
    else:
        print("You lost")
        return False
    
def main():
    '''Main function'''

    # Initial user inputs
    player1 = great()
    casino = House("Casino Royale")
    player1.wallet = float(input("How mcuch money is in your wallet? "))

    # play the first round
    result = player1.bet(casino)
    # Check if bet is greater than wallet
    if result == 1:
        return "You dont have enough moeny, get out of here"
        
    print(f"You have {player1.wallet} in your wallet")
    keep_playing = input("Do you want to keep playing? ")

    # Check for valid input
    while keep_playing.upper() not in ["YES", "NO"]:
        print("Please select valid input. Yes or no")
        keep_playing = input("Do you want to keep playing? ")
    
    while keep_playing.upper() == "YES":
        player1.bet(casino)
        keep_playing = input("Do you want to keep playing? ")
        while keep_playing.upper() not in ["YES", "NO"]:
            print("Please select valid input. Yes or no")
            keep_playing = input("Do you want to keep playing? ")
        if player1.wallet <= 0: 
            return "You have no money, get out of here"

    if keep_playing.upper() == "NO":
        return f"Your final wallet is: {player1.wallet}"

main()
