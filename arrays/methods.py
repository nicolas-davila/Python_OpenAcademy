fruits = ["maca", "banana", "abacaxi"]

print(f"Array base: \n{fruits}")
print("\nArray com append")
fruits.append("pera") # Adiciona "pera" na lista
print(fruits)

print("\nArray com insert")
fruits.insert(1, "uva") # Acrescenta "uva", na posição 1
print(fruits)

print("\n Aray com remove")
fruits.remove("banana") # Remove o elemento "banana" da array
print(fruits)

print("\n Metodo que mostra o elemento removido")
removed_fruit = fruits.pop(2) # Remove o elemento "abacaxi" da array e retorna o próprio elemento
print(fruits)
print(f"Fruta removida: {removed_fruit}")

print("\n Retorna o array em ordem ascendente")
fruits.sort() # Retorna em ordem os elemntos da array
print(fruits)

print("\n Retorna o array em ordem inversa")
fruits.reverse() # Retorna em ordem inversa os elemetos da array
print(fruits)