#!/usr/bin/env python3

a = [int(i) for i in input().split()]

for i in range(1, len(a)):
    if (a[i] > 0 and a[i - 1] > 0) or (a[i] < 0 and a[i - 1] < 0):
        
        print(a[i - 1], a[i])
        break
