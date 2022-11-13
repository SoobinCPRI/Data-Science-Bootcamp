# DECLARANDO LISTAS
grupos = ["Bts", "Exo", "Snuper", "Blackpink"]
print(grupos)

frutas = []
print(frutas)

letras = list("faculdade")
print(letras)

numeros = list(range(10))
print(numeros)

casa = ["porta", 100000, False]
print(casa)

# ACESSO DIRETO
grupos = [1, 2, 3, 4]

print(grupos[0])
print(grupos[-1])

# LISTAS ANINHADAS
matriz = [
    [0, "b", 4],
    ["j", 1, 5],
    ["l", 3, 2]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0] [-1])
print(matriz[-1][-1])

#FATIAMENTO
letras = list("pokemon")

print(letras[2:]) 
print(letras[:2]) 
print(letras[1:3]) 
print(letras[0:3:2])
print(letras[::]) 
print(letras[::-1])

# ITERANDO LISTAS
cama = ["lençol", "colchão", "travesseiro"]

for item in cama:
    print(item, end=", ")
# O for é o melhor para esta função

# FUNÇÃO ENUMERATE PARA VER ÍNDICES
cama = ["lençol", "colchão", "travesseiro"]

for indice, objeto in enumerate(cama):
    print(f"{indice}: {objeto}")

# COMPREENDENDO LISTAS
# Versão mais complicada
numeros = list(range(7))
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Versão simplificada
numeros = list(range(7))
pares = [numero for numero in numeros if numero % 2 == 0]

# Versão mais complicada

numeros = list(range(7))
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

# Versão simplificada
numeros = list(range(7))
quadrado = [numero ** 2 for numero in numeros]




