"""
Napisati kod koji za dati redni broj mjeseca (od 1 do 12) i datu godinu štampa broja dana u
datom mjesecu. 
"""


mjesec = input("Unesite redni broj mjeseca: ")

mjeseci_sa_31 = [1, 3, 5, 7, 8, 10, 12]
mjeseci_sa_30 = [2, 4, 6, 11]

if mjesec in mjeseci_sa_31:
    print("mjesec ima 31 dan")
elif mjesec in mjeseci_sa_30:
    print("mjesec ima 30 dana")
else:
    print("28 ili 29")
