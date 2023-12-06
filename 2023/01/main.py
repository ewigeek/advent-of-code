import sys
import re

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
regexForNumbers = '(?=((?:f(?:ive|our)|s(?:even|ix)|t(?:hree|wo)|(?:ni|o)ne|eight|[0-9])))'

resultingNumber = 0
for line in sys.stdin:
        digits = re.findall(regexForNumbers, line)

        firstDigit = digits[0] if len(digits[0]) == 1 else str(numbers.index(digits[0]))
        lastDigit = digits[-1] if len(digits[-1]) == 1 else str(numbers.index(digits[-1]))

        resultingNumber += int(firstDigit + lastDigit)

print(resultingNumber)