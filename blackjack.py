import random

class Card:
    def __init__(self,value,suit) -> None:
        self.value = value
        self.suit = suit
    
    def __repr__(self) -> str:
        if self.value == 1:
            self.value = "Ace"
        if self.value == 11:
            self.value = "Jack"
        elif self.value ==12:
            self.value = "Queen"
        elif self.value == 13:
            self.value = "King"
        return f"{self.value} of {self.suit}"
    
SUITS = ["spades","hearts","diamonds","Clubs"]

DECK =[Card(value,suit) for value in range(1,14) for suit in SUITS]

def deposit():
    while True:
        amount = input("How much would you like to deposit(Min £10 - Max 1000):£ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 100 and amount < 1000:
                break
            else:
                print("See minimum and maximum deposits amounts please. ")
        else:
            print("Please enter valid amount.No letters" )
    return amount

def deal_cards():
    for i in range(len(DECK)):
        players_cards = [DECK[i], DECK[i+1]]
        house_cards = [DECK[i+2],DECK[i+3]]
        return players_cards,house_cards
        print(type(players_cards))

def player_actions(player_cards):
     while True:
         if player_cards.value.sum() < 21:
             answer = input("press Enter to draw or type No to stop:")
             if answer.lower() == "no":



    







def main():
    random.shuffle(DECK)
    balance = deposit()
    print(deal_cards())
    print(DECK)
    

main()
   


        

        
