# APPEND
lista = [1, "fato", "revista", 5.5]

lista.append("macaco")
print(lista)
# Append só adiciona um objeto por vez

# CLEAR
lista = [1, "fato", "revista", 5.5]

lista.clear()
print(lista)
# Apaga todos os elementos da lista

# COPY
lista = [1, "fato", "revista", 5.5]

lista_1 = lista.copy()
print(lista_1, lista)
# Cria uma cópia da lista

# COUNT
lista = [1, "fato", "revista", 5.5, "fato"]

print(lista.count("fato"))
# Conta o valor informado na lista

# EXTEND
lista = [1, "fato", "revista", 5.5]

lista.extend(["macaco", 5.10])
print(lista)
# Concatena listas

# INDEX
lista = [1, "fato", "revista", 5.5, "fato"]

print(lista.index("fato"))
# Encontra a primeira ocorrência do objeto informado

# POP
lista = [1, "fato", "revista", 5.5]

lista.pop()
print(lista)
lista.pop(1)
print(lista)
# Remove o último valor adicionado à lista, pode-se também indicar o index para remoção

# REMOVE
lista = [1, "fato", "revista", 5.5]

lista.remove("fato")
print(lista)
# Remove o objeto indicado, não se usa o index, mas sim o nome

# REVERSE
lista = [1, "fato", "revista", 5.5]

lista.reverse()
print(lista)
# Espelha a lista

# SORT
lista = ["abelha", "fato", "revista", "rato"]

lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
lista.sort(key=lambda x: len(x))
print(lista)
lista.sort(key=lambda x: len(x))
print(lista)
# Ordena a lista na ordem crescente, decrescente, adiciona uma função e combina a função com ordem decrescente respectivamente

# LEN
lista = [1, "fato", "revista", 5.5]

print(len(lista))
# Vê o tamanho do objeto

# SORTED
lista = ["abelha", "fato", "revista", "macaco"]

sorted(lista, key=lambda x: len(x))
print(lista)
sorted(lista, key=lambda x: len(x), reverse=True)
print(lista)
# A mesma coisa do sort, só que essa é uma função built-in e não um método
