def powerOf8(number):
    
    bitPosition = 0
mask = 1

while (bitPosition <= 63):
    mask <<= bitPosition
    
    
    if (mask == number):
        return True
    
    bitPosition += 3
    mask = 1
    
return False