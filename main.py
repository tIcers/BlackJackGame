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


# 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# 12: Once the user is done, it's time to let the computer play.
# The computer should keep drawing cards as long as it has a score less than 17.


import random

print("Welcome to Blackjack game! ")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

#5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if computer_score > 21 and user_score > 21:
        return "Your score is over 21, you Lose 😭"

    if user_score == computer_score:
        return "Its a draw🥺 "
    elif computer_score == 0:
        return "computer has a blackjack! You lose 😭"
    elif user_score == 0:
        return "You have a blackjack! You won! 😝"
    elif user_score > 21:
        return "Your score is over 21, You lose 😫"
    elif computer_score > 21:
        return "Computer has over 21, Computer lose ☠️"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose..."

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    # 11: The score will need to be rechecked with every new card drawn and the checks in  9
    # need to be repeated until the game ends.

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to draw another card? y or n ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# 13: Create a function called compare() and pass in the user_score and computer_score.
# If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses.
# If the user has a blackjack (0), then the user wins.
# If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses.
# If none of the above, then the player with the highest score wins.



# 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you want to start new game? y or n: ") == "y":

    play_game()










    

