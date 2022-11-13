# WHILE
turno_cadastro = -1

while turno_cadastro != 0:
    turno_cadastro = int(input("Digite o número correspondente ao turno que você deseja ingressar: \n[1] Matutino \n[2] Vespertino \n[3]Noturno \n[0]Sair\n"))

    if turno_cadastro == 1:
        print("Cadastrando em matutino...")
        print("Cadastro concluído!")
        break
    elif turno_cadastro == 2:
        print("Cadastrando em vespertino...")
        print("Cadastro concluído!")
        break
    elif turno_cadastro == 3:
        print("Cadastrando em noturno...")
        print("Cadastro concluído!")
        break

# O while é bom quando não sabemos o número exato de vezes que o código será executado.

while True: # loop infinito
    opcao = int(input("Informe um número: "))

    if opcao == 10:
        break           # break cancela o loop
    elif opcao == 21:   
        continue        # Ignora e segue em frente
    elif opcao > 20:
        print(opcao)
