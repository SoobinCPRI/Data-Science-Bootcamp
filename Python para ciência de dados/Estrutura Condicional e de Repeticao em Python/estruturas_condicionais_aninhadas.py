# IF ANINHADO
conta_universitária = False
conta_normal = True
saldo = 500
limite = 200 
cheque_especial = 250
saque = 800

if conta_normal:
    if saque <= saldo:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com o auxílio do cheque especial.")
    else:
        print("Saque falhou, verifique se você possui saldo suficiente e tente novamente.")
elif conta_universitária:
    if saque <= saldo:
        print("Saque realizado com sucesso!")
    else:
        print("Saque falhou, verifique se você possui saldo suficiente e tente novamente.")
else:
    print("O sistema não reconheceu seu tipo de conta.")