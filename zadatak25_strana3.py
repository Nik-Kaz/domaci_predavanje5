"""
Napisati kod koji za dati redni broj mjeseca (od 1 do 12) i datu godinu štampa broja dana u
datom mjesecu. 
"""

print("Januar, Februar, Mart, April, Maj, Jun, Jul, Avgust, Septembar, Oktobar, Novembar, Decembar")

mjesec = input("Unesite ime mjeseca: ")

if mjesec == "Februar":
    print("Broj dana: 28/29 dana")
elif mjesec in ("April", "Jun", "Septembar", "Novembar"):
    print("Broj dana: 30 dana")
elif mjesec in ("Januar", "Mart", "Maj", "Jul", "Avgust","Oktobar","Decembar"):
    print("Broj dana: 31")   
else:
    print("Unijeli ste pogresano ime mjeseca")      