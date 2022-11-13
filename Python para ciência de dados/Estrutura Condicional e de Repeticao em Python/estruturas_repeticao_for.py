# FOR
palavra = input("Digite a palavra para encontrar as vogais presentes nela: ")
vogais = "aeiou"

for letra in palavra:
    if letra.lower() in vogais:
        print(letra.lower(), end=" ")

#  O for é bom quando nosso objeto é iterável ou quando sabemos a quantidade exata de vezes que nosso código rodará.

# FUNÇÃO RANGE
for numero in range(0, 71, 7): # Parâmetros: início, fim (não inclusivo e único obrigatório) e de quanto em quanto.
    print(numero, end=" ")