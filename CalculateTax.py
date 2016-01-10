#CalculateTax

from Constants import *

def CalculateTax(n):
    Tax = 0
    n = int(n)
    if n <= BAND_ZERO_TAX_LIMIT :
        return int(Tax)
    if n > BAND_ZERO_TAX_LIMIT and n <= BAND_ONE_TAX_LIMIT:
        AmountInBandZero = BAND_ZERO_TAX_LIMIT 
        AmountInBandOne = n - BAND_ZERO_TAX_LIMIT
        Tax = AmountInBandOne * BAND_ONE_TAX
        return int(Tax)
    if n > BAND_ONE_TAX_LIMIT and n <= BAND_TWO_TAX_LIMIT:
        AmountInBandZero = BAND_ZERO_TAX_LIMIT
        AmountInBandOne = BAND_ONE_TAX_LIMIT
        AmountInBandTwo = n - BAND_ONE_TAX_LIMIT
        Tax = AmountInBandOne * BAND_ONE_TAX
        Tax += AmountInBandTwo * BAND_TWO_TAX
        return int(Tax)
    if n > BAND_TWO_TAX_LIMIT:
        AmountInBandZero = BAND_ZERO_TAX_LIMIT
        AmountInBandOne = BAND_ONE_TAX_LIMIT
        AmountInBandTwo = BAND_TWO_TAX_LIMIT
        AmountInBandThree = n - BAND_TWO_TAX_LIMIT
        Tax = AmountInBandOne * BAND_ONE_TAX
        Tax += AmountInBandTwo * BAND_TWO_TAX
        Tax += AmountInBandThree * BAND_THREE_TAX
        return int(Tax)

'''values = [10000,20000,30000,40000,50000,60000,70000,80000,90000]
for value in values:
    print str(value) + "    " + str(CalculateTax(value))'''
