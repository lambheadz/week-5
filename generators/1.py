n = int(input())

def generatesq(n):
    for i in range(1, n + 1):
        yield i ** 2

for x in generatesq(n):
    print(x)

generatesq(n)

##

def geners(N):
    pass
for x in geners(10):
    print(x)
import random
random.randint(1, 10)
def randomn(low, high, n):
    pass
for num in randomn(1, 10, 12):
    print(num)