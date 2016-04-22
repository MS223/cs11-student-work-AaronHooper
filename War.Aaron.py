import random
def shuffle_deck():
    basic_deck = range(2,52)
    random.shuffle(basic_deck)
    return basic_deck

deck = shuffle_deck()

player1 = raw_input("What's your name?")
player2 = raw_input("What's your name?")

player1_score = 0
player2_score = 0

def player_turn(player):
    card = deck.pop()
    player , 'drew' , card
    return str(card)
player_turn(player1)
player_turn(player2)

if player1 > player2:
    player1_score + 1
 elif player_turn(player2) > player_turn(player1):
        player2_score = player2_score + 1

print str(player1)+ " scored " +str(player1_score)
print str(player2)+ " scored " +str(player2_score)
    #need to finish this adding elif and etc 
