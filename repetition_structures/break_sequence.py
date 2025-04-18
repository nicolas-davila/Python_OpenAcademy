print("Quebrando um laço while quando atigir o número 5")

contador = 0
while True:
    print(f"Contador: {contador}")
    contador += 1

    if contador == 5: # Aqui o laço for determina se a variável é igual 5, se sim "break".
        break # Quebra a estrutura de repetição