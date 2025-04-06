def findwater(a, a_size):
    leftTallest = [0]*a_size
    
    water = 0
    
    leftTallest[0] = a[0]
    for i in range( 1, a_size):
        leftTallest[i] = max(leftTallest[i-1], a[i])
        
    rightT