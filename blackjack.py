"""
BlackJack Text Game
"""

import random

dealerBust = 0

#Player
hit = 0
cardOne = random.randint(1,11)
cardTwo = random.randint(1,11)
handTotal = cardOne + cardTwo
print(" Player Card One: ", cardOne, "\n", "Player Card Two: ", cardTwo, "\n", "Player Hand Total: ", handTotal)
while hit == 0:
    if cardOne == 11 and handTotal > 21:
        handTotal = handTotal - 10
        cardOne = 1
        print(" Player Card One: ", cardOne, "\n", "Player Card Two: ", cardTwo, "\n", "Player Hand Total: ", handTotal)
    if cardTwo == 11 and handTotal > 21:
        handTotal = handTotal - 10
        cardTwo = 1
        print(" Player Card One: ", cardOne, "\n", "Player Card Two: ", cardTwo, "\n", "Player Hand Total: ", handTotal)
    if handTotal > 21:
        print(" Player loses.")
        exit()
    hit = int(input(" Do you want to hit? 1 for yes 2 for no. "))
    if hit == 1:
        hitCard = random.randint(1,11)
        handTotal = handTotal + hitCard
        print(" Hit card: ", hitCard)
        print(" Player Hand Total: ", handTotal)
        hit = 0
    else:
        handTotal = handTotal
        print(" Player Hand Total: ", handTotal)

#Dealer
dealerCardOne = random.randint(1,11)
dealerCardTwo = random.randint(1,11)
dealerTotal = dealerCardOne + dealerCardTwo
print(" Dealer Card One: ", dealerCardOne, "\n", "Dealer Card Two: ", dealerCardTwo, "\n", "Dealer Total: ", dealerTotal)
while dealerTotal < 19:
    #hit
    hit = random.randint(1,11)
    dealerTotal = dealerTotal + hit
    print(" Dealer hit: ", hit)
    print(" Dealer Total: ", dealerTotal)
if dealerTotal > 21:
    dealerBust = 1
    print(" Dealer Bust.")

if dealerTotal > handTotal and dealerBust == 0:
    print(" Dealer Wins.")
else:
    print(" Player Wins.")
