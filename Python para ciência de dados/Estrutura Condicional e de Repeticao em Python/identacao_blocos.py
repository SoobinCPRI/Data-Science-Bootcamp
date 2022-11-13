# Python requer blocos identados para funcionar, o padrão são quatro espaços

def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado, obrigado e volte sempre!") #Essa mensagem só é executada caso o if seja satisfeito
    print("Obrigado por ser o nosso cliente!") #Essa mensagem sempre será executada, pois faz parte do método

sacar(600)