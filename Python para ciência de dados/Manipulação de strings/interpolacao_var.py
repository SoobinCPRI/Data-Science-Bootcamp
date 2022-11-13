# OLD STYLE
nome = "Choi Seungyoun"
idade = 25
profissao = "cantor"
fracao = 1.9384
dicionario = {"nome": "Choi Seungyoun", "idade": 25, "profissao": "cantor"}

print("Olá, meu nome é %s, tenho %d anos e sou %s." % (nome, idade, profissao))

# %d = inteiro, %s = string, %f = ponto flutuante

# MÉTODO FORMAT

print("Olá, meu nome é {}, tenho {} anos e sou {}.".format(nome, idade, profissao))

print("Olá, meu nome é {1}, tenho {0} anos e sou {2}.".format(nome, idade, profissao))

print("Olá, meu nome é {nome}, tenho {idade} anos e sou {profissao}.".format(nome = nome, idade = idade, profissao = profissao))

print("Olá, meu nome é {nome}, tenho {idade} anos e sou {profissao}".format(**dicionario))

# F-STRING
print(f"Olá, meu nome é {nome}, tenho {idade} anos e sou {profissao}.")

# Formatação com f-string
print(f"O valor da minha fração em números decimais é: {fracao:4.2f}") # O número na frente do ponto é opcional


