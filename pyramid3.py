#pyramid-3
n = int(input())
for i in range(1,n+1):
    left_spaces = (" ") * (n-i)
    print(left_spaces + ("*"+" ")*i + left_spaces)
m = n
for i in range(1,n):
    spaces = (" ") * i    
    m = m-1
    stars = ("*"+" ")*m
    print(spaces+stars+spaces)