#Longest Collatz Sequence
#Solving for Project Euler.Net Problem 14.
#Given n -> n/2 (n is even)
#      n -> 3n + 1 (n is odd)
#
#Which starting number, under one million, produces the longest chain?
#
#By Alex Murshak




def collatz(n):
    count = 0
    while n>1:
        if n%2==0:
            n= n/2
        else: 
            n= 3*n+1
        count += 1
    return count


C_large = 0
I_large = 0
for i in range(1,1000000,1):
    C = collatz(i)
    if C> C_large:
        C_large = C
        I_large = i
print(I_large)

