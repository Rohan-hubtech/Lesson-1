n = int(input("Enter your number : "))
def checkIfPower(n):
    if(n<=0):   
        return False
    if(n==1):
        return True
    if(n%2==0):
        return checkIfPower(n/2)
    return False
if(checkIfPower(n)):
    print("Power of 2")
else:
    print("Not power of 2")