# FUNÇÕES DEF
def exibir_texto():
    print("Minha primeira função.")
# Função que não aceita argumentos

def exibir_texto_2(parametro):
    print(f"Olá, {parametro}.")
# Função que aceita argumentos, se não declarar vai retornar um erro

def exibir_texto_3(parametro_def="none"):
    print(f"Olá, {parametro_def}.")
# Função que aceita argumentos, mas como há um valor default, não retorna erro caso um valor não seja declarado 

exibir_texto()
exibir_texto_2("Seungyoun")
exibir_texto_3()

# FUNÇÕES COM RETURN
def calcular_razao(numero_1, numero_2):
    return numero_1 * numero_2

def calcular_total(numeros):
    return sum(numeros)

def sucessor_antecessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

print(calcular_razao(9, 16))
print(calcular_total([1,9,90,51]))
print(sucessor_antecessor(17))
# Caso a função não tenha retorno, ele aparecerá "none" com default

# *ARGS E **KWARGS
def exibir_musica(data, *args, **kwargs):
    texto ="\n".join(args)
    meta_dados ="\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_musica("24 de dezembro de 2022", "It's not accident", "It's your fault", "Yeah you know know know know know", autor="Choi Seungyoun", ano=2018)
# Podemos combinar args e kwargs com parâmetros obrigatórios, args recebem tuplas e kwargs dicionários