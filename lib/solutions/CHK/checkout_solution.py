def checkout(skus):
    if not isinstance(skus, str):
        return -1
    
    # to keep track of the prices of each SKU
    prices = { 'A': 50, 'B': 30,'C': 20, 'D': 15,'E': 40,'F': 10 }
    # hold number of occurances for each product
    counts = { 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0 }
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

    cCount = counts['C']
    total += cCount * prices['C']

    dCount = counts['D']
    total += dCount * prices['D']
    return total