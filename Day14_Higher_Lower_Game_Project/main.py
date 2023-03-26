import random
from game_data import data
from art import logo, vs


def data_picker():
    pick = random.randint(0, (len(data) - 1))
    return data[pick]


def print_comparison(to_compare, choice_id):
    print(f"Compare {choice_id}: {to_compare['name']}, {to_compare['description']}, from {to_compare['country']}.")


def higher_lower_game():
    compare_a = None
    compare_b = None
    score = 0
    continue_game = True

    while continue_game:
        if compare_a is None:
            compare_a = data_picker()

        compare_b = data_picker()
        while compare_a == compare_b:
            compare_b = data_picker()

        # print(compare_a)
        # print(compare_b)

        print(logo)

        print_comparison(compare_a, 'A')
        # print(compare_a['follower_count'])

        print(vs)
        print_comparison(compare_b, 'B')
        # print(compare _b['follower_count'])

        player_choice = input("Who has more followers? Type 'A' or 'B':   ").lower()

        if int(compare_a['follower_count']) > int(compare_b['follower_count']) and player_choice == "a":
            score += 1
            print(f"You're right! Current score: {score}")
            compare_a = compare_a
        elif int(compare_a['follower_count']) < int(compare_b['follower_count']) and player_choice == "b":
            score += 1
            print(f"You're right! Current score: {score}")
            compare_a = compare_b
        else:
            print(f"Sorry! You're wrong! Your final score: {score}!")
            continue_game = False


higher_lower_game()
