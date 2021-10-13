"""
Data su tri cijela broja A, B, C. Odrediti da li među njima ima bar jedan paran broj i bar
jedan neparan broj. Ulaz: Prvi red ulaza sadrži tri cijela broja A, B i C (1 ≤ A ≤ 1000). Izlaz:
Štampati „YES“ ili „NO“. 
"""


a = int(input("Unesite a: "))
b = int(input("Unesite b: "))
c = int(input("Unesite c: "))


if a % 2 == 0:
    if b % 2 == 1 or c % 2 == 1:
        print("yes")
    else:
        print("no")
else:
    if b % 2 == 0 or c % 2 == 0:
        print("Yes")
    else:
        print("no")
