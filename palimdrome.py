# TODO: Define a function named 'reverse' that takes an 
# integer and returns the reversed number
def palindrome(n):
    s=0
    
    while n>0:
        r=n%10
        n=n//10
        s=s*10+r
    return s
    







# TODO: Take input from user and use reverse() function to solve the problem
n=int(input())
if palindrome(n)==n:
    print("Yes")
else:
    print("No")
