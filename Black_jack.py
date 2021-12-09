#Black jack

import random
    
class Card:
    def __init__(self,suit,name,card_value):
         #need to identify/create cards for game
        self.suit = suit
        self.name = name
        self.card_value = card_value
    def __repr__(self):
        return repr(self.name)
    

def print_card(names):
    for name in names:
            print(name,'of',suit)
    
        
    
    

        


def Blackjack(deck):
    # need to nest? the deck for the game to know what to use for cards
     #need to make rules for game
    #hand needs to be before score
    player_hand = []
    dealer_hand = []

    player_hand_score = 0
    dealer_hand_score = 0
    
    
    #we need to deal cards but we need 2 cards so we need to set a limit

    while len(player_hand) <2:

        #deal a card
        dealt_card = random.choice(deck)
        player_hand.append(dealt_card)
        #then we have to remove it so it doesnt get dealt twice
        deck.remove(dealt_card)

        #tell player cards and score
        player_hand_score += dealt_card.card_value

        print("Your hand is: ")
        print_card(player_hand)
        print("Your score is: ",(player_hand_score))



        #do the same for dealer except keep a card hidden
        #found out it cant be the same as player so make a new variable

        d_dealt_card = random.choice(deck)
        dealer_hand.append(d_dealt_card)
        deck.remove(d_dealt_card)
        dealer_hand_score += d_dealt_card.card_value


        #print dealers cards, only print first card
        print("Dealers hand is: \n")
        #print_card(dealer_hand[0])
        print("Dealer score is: \n",dealer_hand[0].card_value)

        
        while player_hand_score >21:

            gamble = input("Hit or Stay?")
            gamble
            if gamble == "Hit":
                player_hand.append(dealt_card)
                player_hand_score += player_hand.card_value
                deck.remove(dealt_card)
                #check for ace if over
                if player_hand_score <21 and player_hand[0].card_value == 11:
                    player_hand[0].card_value == 1
                    #forgot to update hand score
                    player_hand_score -= 10

                else:
                    break



            if gamble == "Stay":
                break



        
        
        
        
        
        
        
        
        
        
        
        
        if player_hand_score == 21:
            print("You got blackjack! You win!")
            quit()

        if player_hand_score <21 and dealer_hand_score == 21:
            print("Dealer has blackjack! Dealer win!")

suits = ["Spades","Hearts","Diamonds","Clubs"]
names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_value = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}     


#make a deck
deck = []
for suit in suits:
    for name in names:
        deck.append(Card(suit,name,card_value[name]))

Blackjack(deck)











