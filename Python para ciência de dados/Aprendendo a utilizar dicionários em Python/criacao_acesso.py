# CRIAÇÃO
graduacao = {"curso": "ads", 
            "duracao": 3, 
            "tipo": "tecnólogo"}
# Criando com colchetes

graduacao_1 = dict(curso = "ri", 
                  duracao = 4, 
                  tipo = "bacharelado")
# Criando através do construtor dict

graduacao["status"] = "concluido"
# Adiciona um novo par

print(graduacao, graduacao_1)

# O dicionário é um conjunto não ordenado de pares, as chaves precisam ser objetos imutáveis, mas os valores não

# ACESSO E SUBSTITUIÇÃO DE VALORES
graduacao = {"curso": "ads", 
            "duracao": 3, 
            "tipo": "tecnólogo"}

print(graduacao["curso"])

graduacao["curso"] = "computação"

print(graduacao["curso"])

# DICIONÁRIOS ANINHADOS
contatos = {"jose": {"email": "silva.josecpri@gmail.com", "telefone": "983618597"},
            "andrya": {"email": "andryagab@gmail.com", "telefone": "987991092"},
            "davi": {"email": "davimainyasuo@gmail.com", "telefone": "999849612"}}

print(contatos["jose"]["telefone"])

# ITERANDO DICIONÁRIOS
graduacao = {"curso": "ads", 
            "duracao": 3, 
            "tipo": "tecnólogo"}

for chave in graduacao:
    print(chave, graduacao[chave])

for chave, valor in graduacao.items():
    print(chave, valor)

# A forma mais comum é através do for