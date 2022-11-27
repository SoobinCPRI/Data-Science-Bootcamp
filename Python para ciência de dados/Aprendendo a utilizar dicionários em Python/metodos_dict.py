# MÉTODOS PARA DICIONÁRIOS
# CLEAR
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

contatos.clear()
print(contatos)
# Apaga todos os itens do dicionário

# COPY
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

contatos_2 = contatos.copy()
print(contatos_2)
# Cria uma cópia de um dicionário

# FROMKEYS
contatos = dict.fromkeys(["idade"])
print(contatos)

contatos_2 = dict.fromkeys(["idade"], "vazio")
print(contatos_2)
# Cria chaves, podendo ter um valor nulo ou definido

# GET
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

print(contatos.get("egidio.silva@ufpe.br", {}))
# Pega o valor de uma chave, se essa chave não existir ele retorna um none ou o valor definido

# ITEMS
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

print(contatos.items())
# Retorna uma lista de tuplas com os itens do dicionários, bom para quando se quer iterar

# KEYS
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

print(contatos.keys())
# Retorna as chaves de um dicionário

# POP 
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

contatos.pop("egidio.silva@ufpe.br", {})
print(contatos)
# Retira a chave selecionada e retorna o valor retirado, se ela não existir retorna key error ou o valor definido

# POPITEM
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

contatos.popitem()
print(contatos)
# Retira a chave em ordem, se não tiver nada no dicionário ele dá erro. A diferença pro pop é que o popitem não aceita argumentos

# SETDEFAULT
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

contatos.setdefault("egidio.silva@ufpe.br", "nome")
contatos.setdefault("thiagobrito@ufpe.br", {"nome": "thiago", "telefone": 81983657790})
print(contatos)
# Se a chave existir no dicionário, ele não faz nada, se não existir ele adiciona os argumentos informados

# UPDATE
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

contatos.update({"egidio.silva@ufpe.br": {"nome": "jo", "telefone": 81983618597}})
contatos.update({"thiagobrito@ufpe.br": {"nome": "thiago", "telefone": 81983618598}})
print(contatos)
# Atualiza o nosso dicionário com outro dicionário, se a chave já existir ele vai atualizar a chave, se ela não existir ele ai adicionar a nova chave

# VALUES
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

print(contatos.values())
# Retorna todos os alores do dicionário

# IN
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

print("egidio.silva@ufpe.br" in contatos)
# Verifica se um valor é uma chave em um dicionário

# DEL
contatos ={
    "egidio.silva@ufpe.br": {"nome": "josé", "telefone": 81983618597}
}

del contatos["egidio.silva@ufpe.br"]["nome"]
print(contatos)
# Deleta a chave determina ou todo o dicionário




