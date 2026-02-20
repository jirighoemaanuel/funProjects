import os
print("Welcome to the secret auction program")

still_bidding = True


def clear_screen():
    # Check the operating system name
    if os.name == 'nt':
        # Command for Windows
        _ = os.system('cls')
    else:
        # Command for Linux/macOS (posix is the name for non-Windows)
        _ = os.system('clear')


bidders = {}

while still_bidding:
    name = input("what is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    another_bidder = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n")
    if another_bidder.lower() == 'yes':
        clear_screen()
        continue
    else:
        max_bid = max(bidders.items(), key=lambda item: item[1])
        print(f"The winner is {max_bid[0]} with a bid of ${max_bid[1]}")
        still_bidding = False
