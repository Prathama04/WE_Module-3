import random

def bid(player_name, currency_cards):
    print(f"{player_name}'s turn to bid.")
    print(f"Available currency cards: {currency_cards}")
    
    # Randomly select a bid from available currency cards
    selected_card = random.choice(currency_cards)
    print(f"{player_name} bids {selected_card}.")
    
    return selected_card

def main():
    # Set up players and their currency cards
    player1 = "Player 1"
    player2 = "Player 2"
    player1_currency_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    player2_currency_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Simulate bidding process
    player1_bid = bid(player1, player1_currency_cards)
    player2_bid = bid(player2, player2_currency_cards)
    
    # Determine the winner based on the bids
    if player1_bid > player2_bid:
        print(f"{player1} wins the bid with {player1_bid}.")
    elif player2_bid > player1_bid:
        print(f"{player2} wins the bid with {player2_bid}.")
    else:
        print("Bids are tied. No winner.")

if __name__ == "__main__":
    main()
