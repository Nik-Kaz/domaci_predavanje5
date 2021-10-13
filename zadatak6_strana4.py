"""
Za neku državu poznata je njena površina i broj stanovnika. Odrediti gustinu naseljenosti
te države. 
"""

povrsina = int(input("Unesite povrsinu: "))
br_stanovnika = int(input("Unesite broj stanovnika: "))

gustina_naseljenosti = povrsina / br_stanovnika

print(gustina_naseljenosti)
