#Reverse
def find_rev(n):
  rev=0
  N=n
  while N!=0:
    digit=N%10
    rev=rev*10+digit
    N=N//10
  return rev
print(find_rev(301))\
#Pallindrome
def Pallindrome(n):
    S=n
    rev=0
    while S!=0:
        digit=S%10
        rev=rev*10+digit
        S=S//10
    if S==rev:
        print("Pallindrome")
    else:
        print("Not Pallindrome")
print(Pallindrome(234))
