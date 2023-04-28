#create clear() function
def clear():
    print("\n" * 100)

bids = {}
print("Welcome to the secret auction program")
name = input("please type your name\n")
bids[name] = int(input("please type your bid\n"))
clear()
still = input("Are you done? type yes or no\n")
while(still == "no"):
    name = input("please type your name\n")
    bids[name] = int(input("please type your bid\n"))
    clear()
    still = input("Are you done? type yes or no\n")
for key in bids:
    maxBid = 0 
    winner = ""
    if(bids[key] > maxBid):
        maxBid = bids[key]
        winner = key
print(f"The winner is {winner} with a bid of {maxBid}")