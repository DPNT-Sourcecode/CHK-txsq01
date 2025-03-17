def checkout(skus):
    if not isinstance(skus, str):
        return -1
    
    # to keep track of the prices of each SKU
    prices = { 'A': 50, 'B': 30,'C': 20, 'D': 15,'E': 40,'F': 10,
              'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, '90': 0,
               'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
               'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90, 'Y': 10, 'Z':50}
    # hold number of occurances for each product
    counts = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
               'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
               'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
               'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z':0}
    # total cost
    total = 0

    # iterate through each char of the string 'skus'
    for char in skus:
        # if the char is not from the valid skus, return 1
        if char not in prices:
            return -1
        # otherwise increment the occurances of the product
        counts[char] += 1

    # work out the total cost for the occurances
    aCount = counts['A']

    # first we will check for the 5A deal
    total += (aCount//5) * 200
    aCount = aCount%5
    #then check for 3A deal
    total += (aCount//3) * 130
    total += (aCount % 3) * prices['A']

    eCount = counts['E']
    total += (eCount//2) * 80
    total += (eCount % 2) * prices['E']

    bCount = counts['B']
    freeB = eCount//2
    bCount -= min(freeB, bCount)
    total += (bCount//2) * 45
    total += (bCount % 2) * prices['B']

    fCount = counts['F']
    total += (fCount //3)  * (2 * prices['F'])
    total += (fCount%3) * prices['F']

    for char in skus:
        if counts[char] > 0:
            total += prices[c]
    return total
