import sys
import re
import math

score = 0
amountOfCards = 0

for line in sys.stdin:
        [_, winingCards, myCards] = re.split('\||:', line)

        winingCards = re.findall('[0-9]+', winingCards)
        myCards = re.findall('[0-9]+', myCards)

        amountOfWiningCards = sum(card in myCards for card in winingCards)

        amountOfCards += amountOfWiningCards
        score += math.floor(pow(2, amountOfWiningCards - 1))

       

print(score)
print(amountOfCards)