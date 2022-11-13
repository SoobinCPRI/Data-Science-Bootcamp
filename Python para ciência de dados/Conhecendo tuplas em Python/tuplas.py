# CRIANDO TUPLAS
grupos = ("bts", "exo", "nct",)
letras = tuple("felicidade")
numeros = tuple([1, 2, 3, 4])
pais = ("japao",)
# É uma boa prática que se use vírgulas no fim da tupla para que o Python não a confunda com precedência de operações

# Indexação, fatiamento, aninhamento, fatiamento e iteração funcionam da mesma forma que listas, a principal diferença entre tuplas e listas é que as tuplas são imutáveis

# Devido a essa característica, os métodos da classe tuple são bem menores
print(grupos.count("bts"))
print(grupos.index("nct"))
print(len(grupos))

