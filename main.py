import random
from replit import clear
from art import logo

# Deals a random card
def deal_card():
  """Returns a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Calculates the score
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  # If the sume of cards is 21 and the there are only 2 cards, blackjack
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # If an ace is drawn and the score is greater than 21
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    # Replace 11 with 1
    cards.append(1)
  return sum(cards)

# Compare scores
def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Push"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 🏆"
  else:
    return "You lose 😤"

def play_game():  
  # Import logo
  print(logo)

  # User's cards
  user_cards = []
  # Computer's cards
  computer_cards = []
  # Game condition
  is_game_over = False

  # Deals two cards to user and computer
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    # Calculate scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")

    # If the user score is equal to 0 or 21, or the computer score = 0
    if user_score == 0 or computer_score == 0 or user_score > 21:
      # End game
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      # If user wants another card
      if user_should_deal == 'y':
        # Draw another card
        user_cards.append(deal_card())
      # If user wants to stand
      else:
        # End game
        is_game_over = True

  # Once user is done, the computer draws cards until score is less than 17
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"  Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()