import random
import art
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calculate_score(input_list):
    if sum(input_list) == 21 and len(input_list) == 2:
        return 0
    if sum(input_list) > 21 and 11 in input_list:
        input_list.remove(11)
        input_list.append(1)
    return sum(input_list)

def compare(uscore, cscore):
    if uscore == cscore:
        return "Draw! Equal Score"
    elif cscore == 0:
        return "Lose, opponent has Blackjack"
    elif uscore == 0:
        return "You score blackjack you win!"
    elif uscore > 21:
        return "You lose ! score is over 21"
    elif cscore > 21:
        return " You win ! comp score over 21"
    elif uscore > cscore:
        return " You win , you scored higher!"
    elif cscore > uscore:
        return "You lose, comp score higher than you!"
    else:
        return "You lose for no reason!"
def play_game():
    print(art.logo)
    user_cards = []
    comp_cards = []
    is_game_over = False

    for i in range(0, 2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, Current score: {user_score}")
        print(f"Computer first card: {comp_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score>21:
            is_game_over = True

        else:
            user_should_continue = input("Do you want to draw another card? Y or N").lower()
            if user_should_continue == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score < 17 and computer_score != 0:
        comp_cards.append(deal_card())
        computer_score = calculate_score(comp_cards)

    print(compare(user_score, computer_score))
    print(f"User Cards: {user_cards}, Computer cards: {comp_cards}")

while input("Do you want to play again? Y or No").lower() == "y":
    print("\n" * 20)
    play_game()

