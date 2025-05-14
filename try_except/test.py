try: 
    # Código que pode gerar uma exceção
    result = 10 / 0 # Divisão por 0
    print(result)
except ZeroDivisionError:
    print("Erro! Divisao por zero.")

# Teste personalizado

number = int(input("\nDigite um número a ser dividido por 350: "))

try:
    new_result = 350 / number
    print(new_result)
except ZeroDivisionError:
    print("\nErro na divisão! Número mencionado foi zero.")

# Utilizando Finally

# try:
    # Código que pode gerar uma exceção
#    arquivo = open("arquivo.txt", "r")
    # Realizar operações com o arquivo
# except FileNotFoundError:
#    print("Erro: Arquivo não encontrado")
# finally:
#    arquivo.close()  # Fechar o arquivo sempre, mesmo se ocorrer uma exceção 

# Utilizando funções

def funcao():
    # Código que pode gerar uma exceção personalizada
    divisor = int(input("\nDigite um número para dividir 275: "))
    if divisor == 0:
        raise Exception("\nErro! o número mencionado foi zero.")
    else:
        result_division = 275 / divisor
        print(result_division)
try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")