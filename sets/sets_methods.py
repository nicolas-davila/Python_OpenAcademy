fruits = {"maca", "banana", "abacaxi"}

print(f"Conjunto base: {fruits}")
print("\n Usando o metodo add: ")
fruits.add("pera")
print(fruits)

print("\n Usando o metodo remove")
fruits.remove("banana")
print(fruits)

print("\n Usando o metodo discard")
fruits.discard("uva")
print(fruits) # No caso, não retorna erro, apenas segue o processo

print("\n Usando o metodo clear")
fruits.clear()
print(fruits) # Limpa o conjunto e retorna "set()"