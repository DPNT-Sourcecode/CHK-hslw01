

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    countA = 0
    countB = 0
    countE = 0
    countF = 0
    countH = 0
    countK = 0
    countM = 0
    countN = 0
    countP = 0
    countQ = 0
    countR = 0
    countU = 0
    countV = 0
    total = 0
    
    count20 = 0
    countX = 0
    countZ = 0
    groupbuy = set(['S','T','X','Y','Z'])
    
    cost = {'C':20,'D':15,'G':20,'I':35,
            'J':60,'L':90,'O':10,'S':20,
            'T':20,'W':20,'X':17,'Y':20,'Z':21}
    
    for x in skus:
        if x in groupbuy:
            if x == 'X':
                countX += 1
            elif x == 'Z':
                countZ += 1
            else:
                count20 += 1
            
        elif x in cost:
            total += cost[x]
        elif x == 'A':
            countA += 1
        elif x == 'B':
            countB += 1
        elif x == 'E':
            countE += 1
        elif x == 'F':
            countF += 1
        elif x == 'H':
            countH += 1
        elif x == 'K':
            countK += 1
        elif x == 'M':
            countM += 1
        elif x == 'N':
            countN += 1
        elif x == 'P':
            countP += 1
        elif x == 'Q':
            countQ += 1
        elif x == 'R':
            countR += 1
        elif x == 'U':
            countU += 1
        elif x == 'V':
            countV += 1
        else:
            return -1
     
    # offer for E 
    if countE > 1:
        countB = max(0,countB-(countE)//2)
    
    total += countE*40
    
    # offer for A
    if countA > 4:
            total += ((countA//5)*200)
            countA = countA%5
    
    if countA > 2:
        total += ((countA//3)*130) +  ((countA%3)*50)
    
    else:
        total += 50*countA
    
    # offer for B
    if countB > 1:
        total += ((countB//2)*45) +  ((countB%2)*30)
    
    else:
        total += 30*countB
    
    # offer for F
    if countF > 2:
        countF -= countF//3
    
    total += countF*10
    
    # offer for H
    if countH > 9:
            total += ((countH//10)*80)
            countH = countH%10
    
    if countH > 4:
        total += ((countH//5)*45) +  ((countH%5)*10)
    
    else:
        total += 10*countH
        
    # offer for K
    if countK > 1:
        total += ((countK//2)*120) +  ((countK%2)*70)
    
    else:
        total += 70*countK
        
    # offer for N and M 
    if countN > 2:
        countM = max(0,countM-(countN)//3)
    
    total += countM*15 + countN*40
    
    # offer for P
    if countP > 4:
        total += ((countP//5)*200) +  ((countP%5)*50)
    
    else:
        total += 50*countP
        
    # offer for R
    if countR > 2:
        countQ = max(0,countQ-(countR)//3)
    
    total += countR*50
    
    # offer for Q
    if countQ > 2:
        total += ((countQ//3)*80) +  ((countQ%3)*30)
    
    else:
        total += 30*countQ
        
    # offer for U
    if countU > 3:
        countU -= countU//4
    
    total += countU*40
    
    # offer for V
    if countV > 2:
            total += ((countV//3)*130)
            countV = countV%3
    
    if countV > 1:
        total += ((countV//2)*90) +  ((countV%2)*50)
    
    else:
        total += 50*countV
        
    # groupbuy
    groupbuy = countX + countZ + count20
    
    if groupbuy > 2:
        total += (groupbuy//3)*45
        groupbuy = groupbuy%3
        
    else:
        groupbuy = 0
        total += countX*17+count20*20+countZ*21
    
    if groupbuy > 0:
        
        if countX >= groupbuy:
            total += 17*groupbuy
        
        else:
            total += countX*17
            groupbuy = max(0,groupbuy-countX)
            
            if count20 >= groupbuy:
                total += 20*groupbuy
            
            else:
                total += count20*20
                groupbuy = max(0,groupbuy-count20)
                
                total += groupbuy*21
                    
                    

    
    return total

