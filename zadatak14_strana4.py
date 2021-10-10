"""
Dat je trocifren broj. Odrediti broj koji se dobija zamjenom prve i posljednje cifre.
"""

trocifreni_broj = int(input("Unesite trocifreni broj: "))

prva_cifra = trocifreni_broj // 100
druga_cifra = (trocifreni_broj // 10) % 10
treca_cifra = trocifreni_broj % 10


prva_cifra_opet = prva_cifra

prva_cifra = treca_cifra
treca_cifra = prva_cifra_opet

finalni_broj = (prva_cifra * 100) + (druga_cifra * 10) + treca_cifra
print(finalni_broj)