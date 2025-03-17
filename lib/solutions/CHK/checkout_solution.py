def checkout(skus):
    if not isinstance(skus, str):
        return -1
    
    # to keep track of the prices of each SKU
    prices = { 'A': 50, 'B': 30,'C': 20, 'D': 15,'E': 40,'F': 10,
              'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
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
    counts['A'] = 0

    eCount = counts['E']
    total += (eCount//2) * 80
    total += (eCount % 2) * prices['E']
    counts['E'] = 0

    bCount = counts['B']
    freeB = eCount//2
    bCount -= min(freeB, bCount)
    total += (bCount//2) * 45
    total += (bCount % 2) * prices['B']
    counts['B'] = 0

    fCount = counts['F']
    total += (fCount //3)  * (2 * prices['F'])
    total += (fCount%3) * prices['F']
    counts['F'] = 0

    hCount = counts['H']
    total += (hCount//10) * 100
    hCount = hCount%10
    #then check for 3A deal
    total += (hCount//5) * 45
    total += (hCount % 5) * prices['H']
    counts['H'] = 0

    kCount = counts['K']
    total += (kCount //2)  * 150
    total += (kCount%2) * prices['K']
    counts['K'] = 0

    nCount = counts['N']
    freeM = nCount//3
    mCount = counts['M']
    mCount -= min(freeM, mCount)
    total += mCount * prices['M']
    counts['M'] = 0

    pCount = counts['P']
    total += (pCount//5) * 200
    total += (pCount%5) * prices['P']
    counts['P'] = 0

    qCount = counts['Q']
    freeB = qCount//3
    qCount -= min(freeB, qCount)
    total += (qCount//3) * 80
    total += (qCount%3) * prices['Q']
    counts['Q'] = 0

    uCount = counts['U']
    total += (uCount//4) * (3 * prices['U'])
    total += (uCount%4) * prices['U']
    counts['U'] = 0

    vCount = counts['V']
    total += (vCount//3) * 130
    vCount = vCount%3
    #then check for 3A deal
    total += (vCount//2) * 90
    total += (vCount % 2) * prices['V']
    counts['V'] = 0

    for char in skus:
        if counts[char] > 0:
            total += prices[char] * counts[char]
    return total

