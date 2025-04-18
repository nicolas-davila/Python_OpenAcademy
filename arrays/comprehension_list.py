''' 
Este método cria uma nova array, utilizando outra como base para percorrer utilizando o laço for.
Com isso ele pega o primeiro elemento dentro dela "x" da lista "numbers" e eleva ao quadrado, depois
verifica se esse número elevado é par, com "%2", e então faz o teste lógico com "if", e se for verdadeiro, ele
adciona esse elemento na nova array
'''


numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers if x % 2 == 0] 
print(squared)
