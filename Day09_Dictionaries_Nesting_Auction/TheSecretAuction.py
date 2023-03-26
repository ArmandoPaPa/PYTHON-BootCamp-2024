from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}


def make_a_bid(bids_dictionary):
    print("Welcome to the secret auction program.")

    bidder_name = input("What is your name?: ")
    bid_made = float(input("What is your bid?: $"))
    bids_dictionary[bidder_name] = bid_made

    return bids_dictionary


make_another_bid = True
highest_bid = 0
highest_bidder_name = "---"

while make_another_bid:
    bids = make_a_bid(bids)

    are_there_other_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if are_there_other_bids == "yes":
        clear()
    elif are_there_other_bids == "no":
        clear()
        make_another_bid = False
        for name in bids:
            if bids[name] > highest_bid:
                highest_bid = bids[name]
                highest_bidder_name = name
    else:
        print("Something gone wrong! The auction is Cancelled")
        make_another_bid = False

print(f"The winner is {highest_bidder_name} with a bid of $ {highest_bid}")

print("-" * 40)
print(bids)
