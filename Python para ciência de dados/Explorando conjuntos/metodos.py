# UNION
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))
# Cria um conjunto com a união dos conjuntos 

# INTERSECTION
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))
# Cria um conjunto com a interseção dos conjuntos

# DIFFERENCE
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b))
# Cria um conjunto com a diferença do que tem no conjunto a, mas não no b

# SYMMETRIC DIFFERENCE
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b))
# Cria um conjunto com a diferença entre os dois conjuntos

# ISSUBSET
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
# Pergunta se o conjunto a é um subconjunto de b

# ISSUPERSET
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))
# Pergunta se o conjunto a é a "mãe" (superset) de b

# ISDISJOINT
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}

print(conjunto_a.isdisjoint(conjunto_b))
# Pergunta se o conjunto a não tem interseção com b.

# ADD
grupo = {"jin", "jk"}
grupo.add("rm")

print(grupo)
# Adiciona um objeto a um conjunto. Caso ele já exista, o sistema ignora.

# CLEAR
grupo = {"jin", "jk", "rm"}
grupo.clear()

print(grupo)
# Limpa um set.

# COPY
conjunto_a = {1, 2, 3}
conjunto_b = conjunto_a.copy()

print(conjunto_b)
# Copia um set.

# DISCARD
conjunto_a = {1, 2, 3}
conjunto_a.discard(1)

print(conjunto_a)
# Discarta um elemento do conjunto, se esse elemento não existir ele ignora o comando.

# POP
conjunto_a = {1, 2, 3}
conjunto_a.pop()

print(conjunto_a)
# Discarta o primeiro elemento de um conjunto

# REMOVE
conjunto_a = {1, 2, 3}
conjunto_a.remove(1)

print(conjunto_a)
# É a mesma coisa do discard, porém se você tentar retirar um elemento que não existe ele retornará um erro.

# LEN
conjunto_a = {1, 2, 3}

print(len(conjunto_a))
# Retorna o tamanho de um conjunto

# IN
conjunto_a = {1, 2, 3}

print(1 in conjunto_a)
# Pergunta se um objeto está no conjunto a
