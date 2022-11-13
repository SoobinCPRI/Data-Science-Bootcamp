# UPPER, LOWER e TITLE
palavra = "choi Seungyoun"

print(palavra.lower()) # Todas as letras ficam minúsculas

print(palavra.upper()) # Todas as letras ficam maiúsculas

print(palavra.title()) # A primeira letra de cada palavra fica maiúscula e o restante minúscula

# Retirando espaços extras
palavra_1 = "  Kamisama     "

print(palavra_1.strip()) # Retira espaços extras no início e final da string

print(palavra_1.lstrip()) # Retira espaços extras só no início

print(palavra_1.rstrip()) # Retira espaços extras só no final

# Junção e centralização
palavra_2 = "rato"

print(palavra_2.center(10, '#')) # Centraliza strings, o primeiroargumento é obrigatório e diz quantos espaços a palavra deve ocupar, o segundo é opcional e diz qual caracter deve preencher os espaços que sobraram.

print("faca".join(palavra_2)) # É utilizado com objetos iteráveis, cada iteração adiciona o primeiro argumento ao objeto referenciado.