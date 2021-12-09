#Black jack

import random


    
class Card(object):
    def __init__(self,name,card_value,suit):
         #need to identify/create cards for game
        self.suits = suit
        self.name = name
        self.card_value = card_value
card_value = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}     
name = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suit = ["Spades","Hearts","Diamonds","Clubs"]

#make a deck
deck = []
for name in name:
    for suit in suit:
        deck.append(Card(name,card_value,suit))

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

        player_hand_score += player_hand.card_value
        print("Your hand is: \n",(player_hand))
        print("Your score is: \n",(player_hand_score))



        #do the same for dealer except keep a card hidden
        #found out it cant be the same as player so make a new variable

        d_dealt_card = random.choice(deck)
        dealer_hand.append(d_dealt_card)
        deck.remove(d_dealt_card)
        dealer_hand_score += dealer_hand.card_value


#print dealers cards, only print first card
        print("Dealers hand is: \n",dealer_hand[0])
        print("Dealer score is: \n",dealer_hand[0].card_value)

        
        
        
        
        
        
        
        
        
        
        
        
        
        if player_hand_score == 21:
            print("You got blackjack! You win!")
            quit()

        if player_hand_score <21 and dealer_hand_score == 21:
            print("Dealer has blackjack! Dealer win!")














