# Lendo arquivos

archive = open("dados.txt", "r") # O arquivo deve estar dentro do vscode 'r' de read.
content = archive.read()
print(content)
archive.close()

# Escrevendo arquivos

archive = open("novos_dados.txt", "w") # 'w' de write
archive = ("Olá mundo!")

# Usando comando with