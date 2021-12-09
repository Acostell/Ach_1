#Black jack

import random


class Card:
    def __init__(self,suit,name,card_value):
         #need to identify/create cards for game
        self.suit = suit
        self.name = name
        self.card_value = card_value
    
    #this took me 4 hours to figure out, otherwise name prints hexcode
    def __repr__(self):
        return repr(self.name)
    


def print_card(names):
    for name in names:
            print(name,'of',name.suit)

        
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
names = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_value = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}     


#make a deck
deck = []
for suit in suits:
    for name in names:
        deck.append(Card(suit,name,card_value[name]))    
    

        


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
        p_dealt_card = random.choice(deck)
        player_hand.append(p_dealt_card)
        #then we have to remove it so it doesnt get dealt twice
        deck.remove(p_dealt_card)

        #tell player cards and score
        player_hand_score += p_dealt_card.card_value

        print("Your hand is: ")
        print_card(player_hand)
        print("Your score is: ",(player_hand_score),"\n")



        #do the same for dealer except keep a card hidden
        #found out it cant be the same as player so make a new variable

        d_dealt_card = random.choice(deck)
        dealer_hand.append(d_dealt_card)
        deck.remove(d_dealt_card)
        dealer_hand_score += d_dealt_card.card_value


        #print dealers cards, only print first card
        print("Dealers hand is: ")
        print_card(dealer_hand[:-1])
        print("Dealers score is: ",(dealer_hand_score-(dealer_hand[:1].card_value)))
        

        if  dealer_hand_score == 21 and player_hand_score != 21:
            print("Dealer has blackjack! Dealer wins!")
        elif player_hand_score == 21:
            print("You got blackjack! You win!")
            quit()    
        
    while player_hand_score < 21:

        gamble = input("Hit or Stay?\n")
            
        if gamble == "Hit":
            p_dealt_card = random.choice(deck)
            player_hand.append(p_dealt_card)
            player_hand_score += p_dealt_card.card_value
            deck.remove(p_dealt_card)
            print("Your hand is: ")
            print_card(player_hand)
                
            
                
                
                #check for ace if over

            c_number=0       
            while player_hand_score >21 and player_hand[c_number].card_value == 11:
                player_hand[c_number].card_value = 1
                #forgot to update hand score
                #forgot == is a check so changed to =
                player_hand_score -= 10
                c_number+=1
            print("Your score is: ",(player_hand_score))    

            

        
        elif gamble == "Stay":
            while dealer_hand_score <=16:
                print("Dealer hits")
                d_dealt_card = random.choice(deck)
                dealer_hand.append(d_dealt_card)
                deck.remove(d_dealt_card)
                dealer_hand_score += d_dealt_card.card_value
                print("Dealers hand is: \n")
                print_card(dealer_hand)
                print("Dealers score is: \n",(dealer_hand_score))
            else:
                break

        else:
            print("Hit or Stay?\n")

    if gamble == "Stay":
        while dealer_hand_score <=16:
            d_dealt_card = random.choice(deck)
            dealer_hand.append(d_dealt_card)
            deck.remove(d_dealt_card)
            dealer_hand_score += d_dealt_card.card_value
            print("Dealers hand is: \n")
            print_card(dealer_hand)
            print("Dealers score is: \n",(dealer_hand_score))
            if dealer_hand_score >21:
                print(" Dealer busts")




    if player_hand_score >21:
        print(" You bust! \n Dealer wins!")
        quit()

    elif player_hand_score == 21:
        print("You got blackjack! You win!")
        quit()

    if  dealer_hand_score == 21 and player_hand_score != 21:
        print("Dealer has blackjack! Dealer wins!")
        quit()

    elif player_hand_score == dealer_hand_score:
        print(" Tie game!")
        quit

    if player_hand_score > dealer_hand_score and dealer_hand_score <21:
        print("Player wins!")
        quit()

    if player_hand_score < dealer_hand_score and dealer_hand_score <21:
        print("Dealer wins!") 
        quit()   


Blackjack(deck)











