# Desafio
# Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao lorde do mal, Sauron. Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de Angmar, um dos Nazgûl (antigos reis humanos que foram corrompidos pelos poderes dos anéis de Sauron). Saruman comanda a torre de Orthanc, onde cria seus servos Uruk-hai, orcs mais terríveis que os convencionais. Para comunicação, eles utilizam as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres.
# A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a acometem diariamente. Um dos problemas que tem atrapalhado sua população é a Interferência de Comunicação Mágica (ICM). Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que para calcular o ICM para Palantír’s, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos. Gandalf, o Cinza, chegou a questionar essa conclusão, alegando que ela não fazia muito sentido, mas ele mesmo concluiu que dar sentido às coisas não faz sentido.
# Saruman e Sauron precisam de uma comunicação estável, pois têm medo que Frodo e seus amigos consigam atrapalhar seus planos, portanto, querem saber quanto de ICM há na comunicação de seus Palantír’s, para que saibam quanto de magia devem empregar na comunicação.

# Entrada
# A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.

# Saída
# Um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais.


# Exemplos de Entrada	  Exemplos de Saída
# 100 2 2                   25.00

# Resposta
entrada = input().split()

distancia = int(entrada[0])
diametro_1 = int(entrada[1])
diametro_2 = int(entrada[2])

ICM = distancia / (diametro_1 + diametro_2)
print(f"{ICM:.2f}")

# Aprimoramento de código pessoal
entrada_1 = int(input("Digite a distância entre os Palantir: "))
while entrada_1 < 0 or entrada_1 > 10000:
      entrada_1 = int(input("Número incorreto! Digite a distância entre os Palantir novamente: "))

entrada_2 = int(input("Digite o diâmetro do Palantir de Sauron: "))
while entrada_2 < 0 or entrada_2 > 100:
      entrada_2 = int(input("Número incorreto! Digite o diâmetro do Palantir de Sauron novamente: "))

entrada_3 = int(input("Digite o diâmetro do Palantir de Saruman: "))
while entrada_3 < 0 or entrada_3 > 100:
      entrada_3 = int(input("Número incorreto! Digite o diâmetro do Palantir de Saruman novamente: "))

ICM = entrada_1 / (entrada_2 + entrada_3)
print(f"A interferência de comunicação mágica é de: {ICM:.2f}")
