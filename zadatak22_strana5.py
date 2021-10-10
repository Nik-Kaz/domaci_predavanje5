"""
Napišite program koji će odrediti ukupan broj tačkica na svim pločicama u potpunom
skupu domina veličine N. Vaš program treba da učita jedan prirodan broj N (1 ≤ N ≤ 1000)
– veličinu potpunog skupa domina. Program treba da štampa ukupan broj tačkica na svim
pločicama u potpunom skupu domina veličine N. 
"""


"""Provjera da li u nizu postoje domine potpuno istih oznaka """


def postoji_domina(i, j, niz):
    for x in niz:
        if ((x[0] == i and x[1] == j) or (x[0] == j and x[1] == i)):
            return True
    return False


"""" Dodavanje domina u nizu ako ne postoji """


def dodaj_niz_domina(i, j, niz):
    if len(niz) == 0:
        niz.append([i, j])
    if not postoji_domina(i, j, niz):
        niz.append([i, j])


""" Suma tackica na svim dominama u nizu""""


def suma_tackica():
    n = int(input("Unesite najveci broj tackica: "))
    suma = 0
    niz_domina = []
    for i in range(n + 1):
        for j in range(n + 1):
            dodaj_niz_domina(i, j, niz_domina)
    for x in niz_domina:
        suma = x[0] + x[1] + suma
    return suma


print(suma_tackica())
