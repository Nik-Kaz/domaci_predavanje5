"""
Dat je realan broj a. Koristeći samo operaciju množenja i pomoćne promjenljive,
izračunati:
a. a7
za 4 operacije
b. a10 za 4 operacije
c. a21 za 6 operacija
d. a64 za 6 operacija
e. a3 i a10 za 4 operacije
f. a2
, a
5 i a17 za 6 operacija 
"""


def pod_a():
    a = int(input("Unesite broj: "))
    a2 = a * a
    a4 = a2 * a2
    a8 = a4 * a4
    return a8 / a


def pod_b():
    a = int(input("Unesite broj: "))
    a2 = a * a
    a4 = a2 * a2
    a8 = a4 * a4
    return a8 * a2


def pod_c():
    a = int(input("Unesite broj: "))
    a2 = a * a
    a4 = a2 * a2
    a8 = a4 * a4
    a16 = a8 * a8
    a20 = a16 * a4
    return a20*a


def pod_d():
    a = int(input("Unesite broj: "))
    a2 = a * a
    a4 = a2 * a2
    a8 = a4 * a4
    a16 = a8 * a8
    a32 = a16 * a16
    return a32*a32


def pod_e():
    a = int(input("Unesite broj: "))
    a2 = a * a
    a3 = a2 * a
    a5 = a3 * a2
    a10 = a5*a5
    print(f"a na stepen 3 je {a3}, a a na stepen 10 je {a10}")


def pod_f()


a = int(input("Unesite broj: "))
a2 = a * a
a4 = a2 * a2
a5 = a4 * a
a10 = a5*a5
a15 = a10*a5
a17 = a15*a2
print(
    f"a na stepen 2 je {a2}, a a na stepen 5 je {a5} i a na stepen 17 je {a17}")
