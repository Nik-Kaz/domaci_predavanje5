"""
Fudbal – Petar je posmatrao fudbalsku utakmicu i na papiru zapisivao rezultat sa
semafora poslije svakog gola. Npr. mogući zapis je: 1:0, 1:1, 1:2, 2:2, 2:3. Zatim je Petar
sabrao sve zapisane brojeve: 1+0+1+1+1+2+2+2+2+3=15. Na osnovu datog zbira, 
napišite program koji određuje koliko je golova bilo na utakmici. Ulaz: U jednom redu dat
je cio broj N – Petrov zbir (1 ≤ N ≤1000). Izlaz: Štampati jedan cio broj – broj golova.
"""


def ukupan_broj_golova():
    n = int(input("unesite broj golova: "))
    s = 0
    i = 0
    while n > s:
        i = i + 1
        s = s + i
    return i


print(ukupan_broj_golova())
