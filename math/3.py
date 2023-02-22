from math import *
nside = int(input())
slen = int(input())
area = nside * (slen ** 2) / (4 * tan(pi / nside))
print(area)