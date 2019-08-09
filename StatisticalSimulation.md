```py
# Shuffle deck & count card occurrences in the hand
n_sims, two_kind = 10000, 0
for i in range(n_sims):
    np.random.shuffle(deck_of_cards)
    hand, cards_in_hand = deck_of_cards[0:5], {}
    for card in hand:
        # Use .get() method on cards_in_hand
        cards_in_hand[card[1]] = cards_in_hand.get(card[1], 0) + 1
    
    # Condition for getting at least 2 of a kind
    highest_card = max(cards_in_hand.values())
    if  highest_card>=2: 
        two_kind += 1

print("Probability of seeing at least two of a kind = {} ".format(two_kind/n_sims))
```
