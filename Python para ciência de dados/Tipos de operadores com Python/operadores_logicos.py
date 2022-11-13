# AND = Para que seja True, todos os valores precisam ser True
# OR = Para que seja True, basta que um dos valores seja True
# NOT = Inverso do resultado
# () = a mesma coisa de um parênteses em uma conta

# Saque no banco

saldo = 1200
saque = 250
limite = 200
conta_especial = True 

# Para que o usuário saque, o saldo precisa ser maior ou igual ao saque e o saque precisa ser menor que o limite diário.
conta_comum = saldo >= saque and saque <= limite 

# Se o usuário tiver conta especial, ele pode ignorar o limite, porém precisa que o saldo seja maior ou igual ao saque.
conta_especial = conta_especial and saldo >= saque 

# Resultado de teste com as definições do usuário: 
checagem_usuário = conta_comum or conta_especial
print(checagem_usuário)
