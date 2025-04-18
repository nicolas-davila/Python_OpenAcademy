# keys(): Retorna uma visualização de todas as chaves do dicionário

pessoa = {"nome": "Nicolas", "idade": 20, "cidade": "Itajuba"}
print(pessoa.keys()) # Irá imprimir as "variáveis" criadas na estrutura dados

# values(): Retorna uma visualização de todos os valores do dicionário
# Reutilizando a mesma variável criada antes
print(pessoa.values()) # Retorna os valores da variável criada

# items(): Retorna uma visualização de todos os pares chave-valor do dicionário
# Reutilizando a mesma variável criada antes
print(pessoa.items()) # Retorna chave-valor

# update(outro_dicionario): Atualiza a estrutura de dados com os pares chave-valor
# Reutilizando a mesma variável criada antes
pessoa.update({"profissao": "Programador Junior"})
print(pessoa) # Retorna as variaveis com os valores (chave-valor)