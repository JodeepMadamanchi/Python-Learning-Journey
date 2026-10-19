from art import logo
print(logo)

bids = {}
game_over = False
while not game_over:
    name = input("What is your name?:  ")
    bid =  int(input("What is your bid?:  "))
    bids[name] = bid
    should_continue = input("Are theere any other bidders. Type 'yes' or 'no'").lower()
    if should_continue == 'no':
        game_over = True
    elif should_continue == 'yes':
        print("\n" * 50)

highest_bid = 0
winner = ""
for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
print(f"THE HIGHEST BID is {highest_bid} BY {winner}")


