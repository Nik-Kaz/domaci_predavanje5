import math

"""
Napisati kod koji za date katete a i b (a<b) pravouglog trougla računa površinu i
zapreminu tijela koje se dobija rotacijom trougla oko manje katete.
"""


"""
r je poluprecnik
h je visina
s je stranica kupe

"""


def zapremina_povrsine():
    a = int(input("unisete prvu katetu: "))
    b = int(input("unisete drugu katetu: "))
    r = 0
    h = 0
    s = 0
    if a > b:
        r = a
        h = b
    else:
        r = b
        h = a

    s = math.sqrt(pow(a, 2) + pow(b, 2))

    p = math.pi * pow(r, 2) + (math.pi * r * s)
    v = (math.pi * pow(r, 2) * h) / 3

    return(f"Povrsina je {round(p,2)}. Zapremina {round(v,2)}")


print(zapremina_povrsine())
