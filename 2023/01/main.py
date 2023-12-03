import sys
import re

resultingNumber = 0
for line in sys.stdin:
        firstDigit = re.search(r'[0-9]', line).group()
        secondDigit = re.search(r'[0-9]', line[::-1]).group()
        resultingNumber += int(firstDigit + secondDigit)

print(resultingNumber)