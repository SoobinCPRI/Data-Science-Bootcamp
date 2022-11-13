# CRIANDO SETS
tupla_conjunto = set(("palio", "gol", "celta", "palio")) # É possível declarar um set utilizando o construtor set
print(tupla_conjunto)

lis_conjunto = set([1, 3, 4, 5, 3])
print(lis_conjunto)

letras = set("abacaxi")
print(letras)

conjunto = {1, 5, 9, 1} # É possível declarar um set utilizando colchetes ou com construtor
print(conjunto)
# Sets são coleções de objetos que não possuem repetições, eles funcionam como a teoria dos conjuntos
# Não confie nas ordens que o set trará

# ACESSANDO SETS
conjunto_1 = {1, 5, 9, 11}
convercao = list(conjunto_1)

print(convercao[0])
# Sets não permitem indexação, você deve convertê-lo para uma lista

# ITERANDO CONJUNTOS
conjunto_1 = {1, 5, 9, 11}

for numero in conjunto_1:
    print(numero, end=", ")
# A forma mais comum de se percorrer pelos conjuntos é através do for, que também permite enumerate

