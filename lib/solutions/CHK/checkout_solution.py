# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    # to keep track of the prices of each SKU
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    # hold number of occurances for each product
    counts = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0
    }

    # total cost
    total = 0

    # iterate through each char of the string 'skus'
    for char in skus:
        # if the char is not from the valid skus, return 1
        if char not in prices:
            return -1
        # otherwise 
        counts[char] += 1

    aCount = counts['A']
    total += (aCount//3) * 130
    total += (aCount % 3) * prices['A']

    bCount = counts['B']
    total += (bCount//2) * 45
    total += (bCount % 2) * prices['B']

    cCount = counts['C']
    total += cCount * prices['C']

    dCount = counts['D']
    total += dCount * prices['D']


