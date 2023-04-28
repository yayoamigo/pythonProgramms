import random
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if start == 'y':
    cards = {
    "Ace of Spades": 11,
    "2 of Spades": 2,
    "3 of Spades": 3,
    "4 of Spades": 4,
    "5 of Spades": 5,
    "6 of Spades": 6,
    "7 of Spades": 7,
    "8 of Spades": 8,
    "9 of Spades": 9,
    "10 of Spades": 10,
    "Jack of Spades": 10,
    "Queen of Spades": 10,
    "King of Spades": 10,
    "Ace of Hearts": 11,
    "2 of Hearts": 2,
    "3 of Hearts": 3,
    "4 of Hearts": 4,
    "5 of Hearts": 5,
    "6 of Hearts": 6,
    "7 of Hearts": 7,
    "8 of Hearts": 8,
    "9 of Hearts": 9,
    "10 of Hearts": 10,
    "Jack of Hearts": 10,
    "Queen of Hearts": 10,
    "King of Hearts": 10,
    "Ace of Diamonds": 11,
    "2 of Diamonds": 2,
    "3 of Diamonds": 3,
    "4 of Diamonds": 4,
    "5 of Diamonds": 5,
    "6 of Diamonds": 6,
    "7 of Diamonds": 7,
    "8 of Diamonds": 8,
    "9 of Diamonds": 9,
    "10 of Diamonds": 10,
    "Jack of Diamonds": 10,
    "Queen of Diamonds": 10,
    "King of Diamonds": 10,
    "Ace of Clubs": 11,
    "2 of Clubs": 2,
    "3 of Clubs": 3,
    "4 of Clubs": 4,
    "5 of Clubs": 5,
    "6 of Clubs": 6,
    "7 of Clubs": 7,
    "8 of Clubs": 8,
    "9 of Clubs": 9,
    "10 of Clubs": 10,
    "Jack of Clubs": 10,
    "Queen of Clubs": 10,
    "King of Clubs": 10
}
    playerCards = {}
    computerCards = {}

    def getCards(player):
        randomkey = random.choice(list(cards.keys()))
        player[randomkey] = cards[randomkey]
        del cards[randomkey]
    
    def countCards(player):
        count = 0
        for key in player:
            count += player[key]
        return count
    
    getCards(playerCards)
    getCards(playerCards)
    getCards(computerCards)
    print(f"your cards are {list(playerCards.keys())} \n")
    print(f"computer cards are {list(computerCards.keys())} \n")

    another = input("type y to get another card or n to stop: ")
    playerLost = False
    while another == "y":
        getCards(playerCards)
        counter = countCards(playerCards)
        if(counter <= 21):
            print(f"your cards are {list(playerCards.keys())} \n")
            another = input("type y to get another card or n to stop: ")   
        else:
            another = "n"
            playerLost = True
    
    if playerLost == False:
        getCards(computerCards)
        print(f"computer cards are {list(computerCards.keys())} \n")
        compuerCounter = countCards(computerCards)
        if(compuerCounter > 21):
            print("computer went over 21 you win")
        elif(compuerCounter == 21):
            print("computer got 21 you loose")
            playerLost = True
        elif(compuerCounter < 13):
            print("computer got less than 17 so it will get another card")
            getCards(computerCards)
            print(f"computer cards are {list(computerCards.keys())} \n")
            compuerCounter = countCards(computerCards)
            if(compuerCounter > 21):
                print("computer went over 21 you win")
                playerLost = True
            elif(compuerCounter == 21):
                print("computer got 21 you loose")
                playerLost = True
        else:
            finalPlayerCount = 21 - countCards(playerCards) 
            finalComputerCount = 21 - countCards(computerCards)
            if(finalPlayerCount < finalComputerCount):
                print("you win")
            else:
                print("you loose")
    else:
     print(f"you went over 21 your cards are {list(playerCards.keys())}")


else:
 print('have a nice day')

