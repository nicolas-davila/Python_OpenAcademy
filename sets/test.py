fruits = {"maca", "banana", "abacaxi"}
numbers = set({1, 2, 3, 4, 5,})

first_set = {1, 2, 3}
second_set = {3, 4, 5}

print("Usando o simbolo de uniao")
coupling = first_set | second_set
print(coupling) # Retorna a junção dos conjuntos

print("\n Usando o simbolo de intersecao")
intersection = first_set & second_set
print(intersection) # Retorna o número que intercede entre ambos os conjuntos

print("\n Usando o simbolo de diferenca")
difference = first_set - second_set
print(difference) # Retorna com um novo conjunto que mostra quais elementos possui no conjunto1 mas não no conjunto2

print("\n Usando o simbolo de diferenca simetrica")
symmetric_difference = first_set ^ second_set
print(symmetric_difference) # Retorna um novo conjunto que une os dois mas não se tiver o mesmo valor em ambos
