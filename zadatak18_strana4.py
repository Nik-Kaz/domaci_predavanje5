"""
Dat je cio broj k (1<=k<=180) i niz cifara 10111213...9899 koji se dobija kada se svi
dvocifreni brojevi redom zapišu jedan iza drugog. Za dato k, odrediti dvocifreni broj koji
sadrži k-tu cifru u datom nizu. Npr., za k=7, traženi broj je 13.
"""
k = int(input("Unesite broj izmedju 1 i 180: "))

while k < 1 or k > 180:
    k = int(input("Unesite broj izmedju 1 i 180: "))


niz = ""
i = 10
rezultat = ""


while i < 100:
    niz += str(i)
    i += 1

if k % 2 == 0:
    rezultat = niz[k:k+2]
else:
    rezultat = niz[k-1:k+1]

print(rezultat)
