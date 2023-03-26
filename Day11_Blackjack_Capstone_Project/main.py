import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

""""
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# print("Your cards: [..., ...]")
# print("Computer's first card: ...")
# print("Type 'y' to get another card, type 'n' to pass:    ")
# print("Your final hand: [ ]")
# print("Computer's final hand: [ ]")
# print("You win! Lose! Draw!")
# print("Do you want to play a game of Blackjack? Type 'y' or 'n':   ")


def black_jack_game(_cards):
    player_cards = []
    computer_cards = []

    # Player first cards:
    for n in range(0, 2):
        card_picked = random.choice(_cards)
        player_cards.append(card_picked)

    # Computer first cards:
    for m in range(0, 2):
        card_picked = random.choice(_cards)
        computer_cards.append(card_picked)

    # print(player_cards)
    # print(computer_cards)
    # print("-" * 23)

    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

    pick_one_more_card = None
    player_card_count = player_cards[0] + player_cards[1]
    computer_card_count = computer_cards[0] + computer_cards[1]

    while pick_one_more_card != "n":
        if player_card_count <= 21:
            pick_one_more_card = input("Type 'y' to get another card, type 'n' to pass:    ").lower()
            if pick_one_more_card == "y":
                player_cards.append(random.choice(_cards))
                player_card_count += player_cards[-1]

                print(player_cards)
                print(player_card_count)

                if player_card_count > 21:
                    for k in range(0, len(player_cards)):
                        if player_cards[k] == 11:
                            player_cards[k] = 1
                            print("You have ACE (11 p), it will turn into 1 p!")
                            break
                    player_card_count = 0
                    for p in range(0, len(player_cards)):
                        player_card_count += player_cards[p]
        else:
            print(f"Your final hand: {player_cards} = {player_card_count}. YOU LOSE!")
            break

    if player_card_count <= 21:
        while computer_card_count < 17:
            computer_cards.append(random.choice(_cards))
            computer_card_count += computer_cards[-1]

        while computer_card_count > 21 and 11 in computer_cards:
            for t in range(0, len(computer_cards)):
                if computer_cards[t] == 11:
                    computer_cards[t] = 1
                    print("Computer has ACE (11 p), it will turn into 1 p!")
                    break
            computer_card_count = 0
            for u in range(0, len(computer_cards)):
                computer_card_count += computer_cards[u]

        if computer_card_count > 21:
            print(f"Your final hand: {player_cards} = {player_card_count}. YOU WIN!")
            print(f"Computer final: {computer_cards} = {computer_card_count}.")

        elif player_card_count > computer_card_count:
            print(f"Your final hand: {player_cards} = {player_card_count}. YOU WIN!")
            print(f"Computer final: {computer_cards} = {computer_card_count}.")
        elif player_card_count == computer_card_count:
            print(f"Your final hand: {player_cards} = {player_card_count}.")
            print(f"Computer final: {computer_cards} = {computer_card_count}.")
            print("----- D R A W -----")
        else:
            print(f"Your final hand: {player_cards} = {player_card_count}. YOU LOSE!")
            print(f"Computer final: {computer_cards} = {computer_card_count}. COMPUTER WINs!")

    # print(player_cards)
    # print(computer_cards)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n':   ") == "y":
    print(logo)
    black_jack_game(cards)
