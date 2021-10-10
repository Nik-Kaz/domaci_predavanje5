"""
Napisati kod koji za datu godinu odreñuje da li je prestupna i štampa odgovarajuću
poruku. 
"""

godina = int(input("Unesite godinu: "))

if godina % 4 == 0:
    if godina % 100 == 0:
        if godina % 400 == 0:
            print("Prestupna godina")
        else:
            print("Nije prestupna godina")
    else:
        print("Prestupna godina")
else:
    print("Nije prestupna godina.")                