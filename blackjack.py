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

        # Handle no money or no valid input
        if self.wallet <= 0:
            return 1
        elif user_bet > self.wallet:
            print("You Dont have enough money")
            return self.bet(house)
        elif user_bet <= 0:
            print("Your bet must be a positive integer")
            return self.bet(house)
        
        # Handle the game it self
        results = blackjack(self, house)
        if results is True: #Player wins
            self.wallet += user_bet
            print(f"You made ${user_bet}")
            self.wins += 1
            house.loses += 1
            return 
        
        elif results is False: #Player loses 
            self.wallet -= user_bet
            self.loses += 1
            house.wins += 1
            print(f"House wins. You lost ${user_bet}")
            return 0

        elif results == None: #its a draw
            print("Its a draw, no one wins")
            return 0
        
        

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
                ace_value = Ace_house_checker(total_value)
                total_value += deck_cards[ace_value]
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
                ace_value = Ace_checker()
                total_value += deck_cards[ace_value]
        elif card in deck_cards:
            total_value += deck_cards[card]
    return total_value


def players_game(player):
    '''Black Jack Game'''
    # First movement
    player.cards = [] # resets the cards
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
    house.cards = [] #resets the cards
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
        player.total = player_count(player)
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

    

    # House tourn to take a card
    casino.total = blackjack_dealer(casino)

    # Chceck all possible outocmes

    # both above 21
    if casino.total > 21 and player1.total > 21:
        return None
    
    # Check if player exceed 21
    elif player1.total > 21:
        return False 
    
    elif casino.total > 21:
        return True

    # player and casino have the same number | Draw
    elif player1.total == casino.total:
        return None
    
    # Player have higher cards than casino | Player wins
    elif player1.total > casino.total:
        return True
    
    # House higher card than player | House wins
    else :
        return False
    

def main():
    '''Main function'''

    # Initial user inputs
    player1 = great()
    casino = House("Casino Royale")
    player1.wallet = float(input("How much money is in your wallet? "))

    # play the first round
    print("\n--- NEW ROUND ---")
    result = player1.bet(casino)
    # Check if bet is greater than wallet
    if result == 1:
        return "You dont have enough moeny, get out of here"
        
    print(f"You have {player1.wallet} in your wallet")
    
    keep_playing = "YES"
    
    while keep_playing.upper() == "YES":
        print("\n--- NEW ROUND ---")

        if player1.wallet <= 0:
            return "You dont have enough moeny, get out of here"

        # Play the next round
        result = player1.bet(casino)

        # User ran out of money
        if player1.wallet <= 0 or result == 1:
            return "You dont have enough moeny, get out of here"

        # Play another round
        keep_playing = input("Do you want to keep playing? ")

        # Chck for valid input
        while keep_playing.upper() not in ["YES", "NO"]:
            print("Please select valid input. Yes or no")
            keep_playing = input("Do you want to keep playing? ")
        
    # Exit message
    if keep_playing.upper() == "NO":
        return f"Your final wallet is: {player1.wallet}"

main()
