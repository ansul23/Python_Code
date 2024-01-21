def find_rev(n):
  rev=0
  N=n
  while N!=0:
    digit=N%10
    rev=rev*10+digit
    N=N//10
  return rev
print(find_rev(301))
