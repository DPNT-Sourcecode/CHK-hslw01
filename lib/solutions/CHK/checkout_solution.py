

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    countA = 0
    countB = 0
    total = 0
    
    for x in skus:
        if x == 'A':
            countA += 1
        elif x == 'B':
            countB += 1
        elif x == 'C':
            total += 20
        elif x == 'D':
            total += 15
        else:
            return -1
        
    if countA > 2:
        total += ((countA//3)*130) +  ((countA%3)*50)
    
    else:
        total += 50*countA
        
    if countB > 1:
        total += ((countB//2)*45) +  ((countB%2)*30)
    
    else:
        total += 30*countB
        
    return total
