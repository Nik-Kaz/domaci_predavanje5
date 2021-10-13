"""
Za prirodan broj k, štampati frazu „Na izletu smo ubrali k pecuraka“, gdje završetak riječi
„pečurka“ prilagodite broju k. Npr. 101 pecurku, 1204 pecurke, 506 pecuraka. 
"""


def pecurki_helter(k):
    sufix = ""
    if k < 10:
        if k == 1:
            sufix += "ku"
        elif k in [2, 3, 4]:
            sufix += "ke"
        else:
            sufix += "aka"
    elif k < 20:
        sufix += "ki"
    else:
        return pecurki_helter(k % 10)
    return sufix


def stampa_pecurki():
    k = int(input("Unesite broj: "))
    x = k
    br_pecurki = "pecur"
    if x > 100:
        x = x % 100
    br_pecurki += pecurki_helter(x)
    print(f"Na izletu smo ubrali {k} {br_pecurki}")


print(stampa_pecurki())
