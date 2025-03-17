# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if not isinstance(skus, str):
        return -1
    
    prices = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    counts = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0
    }

    total = 0

    for char in skus:
        if char not in prices:
            return -1
        counts[c]


