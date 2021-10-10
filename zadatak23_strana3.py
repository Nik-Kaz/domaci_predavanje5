"""Date su dvije promjenljive x i y istog tipa. Napisati kod koji mijenja mjesta vrijednostima u
promjenljivim x i y. Npr. ako je x = 5 i y = 10, poslije izvršavanja koda treba da bude x=10 i
y=5. """


x = 5
y = 10

x, y = y, x
print(x, y)