# Desafio
# Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu carro faz 12 KM/L. Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda. Para efetuar o cálculo, deve-se fornecer o tempo gasto em horas na viagem e a velocidade média durante a mesma em km/h. Assim, você conseguirá passar para Rubens qual a distância percorrida e, em seguida, calcular quantos litros serão necessários para a viagem que ele quer fazer. Mostre o valor com 3 casas decimais após o ponto.

# Entrada
# O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

# Saída
# Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

 
# Exemplo de Entrada	Exemplo de Saída
# 10 85                 70.833

# Resposta
entrada = input().split()

tempo_h = int(entrada[0])
velocidade_mean = int(entrada[1])

consumo_gas = tempo_h * velocidade_mean / 12

print(f"{consumo_gas:.3f}")

# Aprimoramento de código pessoal
entrada_1 = int(input("Digite o tempo gasto na viagem (horas): "))
entrada_2 = int(input("Digite a velocidade média em que estava durante a viagem: "))
consumo_gas = entrada_1 * entrada_2 / 12

print(f"{consumo_gas:.3f}")  