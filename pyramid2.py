#pyramid-2
n = int(input())
for i in range(1,n+1):
    left_spaces = (" ") * (n-i)
    print(left_spaces + ("*"+" ")*i + left_spaces)
    