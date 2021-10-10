"""
Date su stranice a i b pravougaonika. Naći njegov obim i površinu. 
"""

a = int(input("Unesite stranicu a pravougaonika: ")) 
b = int(input("Unesite stranicu b pravougaonika: ")) 

povrsina = a * b
obim = (2*a) + (2*b)

print(f"Povrisna pravougaonika je {povrsina}, a obim je {obim}")