import random


def gerar_lista_ordenadaCrescente(size):
    lista = list(range(size + 1))  # Cria uma lista de valores de 0 a 1000
    # Converte os valores em formato de texto e os junta separados por quebras de linha
    lista_texto = '\n'.join(str(valor) for valor in lista)

    with open('/home/pixies0/UFT/PAA/PAA/src/inputs/' + str(size) + 'ASC.txt', 'w') as arquivo:
        arquivo.write(lista_texto)  # Escreve a lista no arquivo de texto


def gerar_lista_ordenadaDecrescente(size):
    # Cria uma lista de valores de 1000 a 0 em ordem decrescente
    lista = list(range(size, -1, -1))
    # Converte os valores em formato de texto e os junta separados por quebras de linha
    lista_texto = '\n'.join(str(valor) for valor in lista)

    with open('/home/pixies0/UFT/PAA/PAA/src/inputs/' + str(size) + 'DESC.txt', 'w') as arquivo:
        arquivo.write(lista_texto)  # Escreve a lista no arquivo de texto


def gerar_lista_ordenadaAleatoria(size):
    lista = list(range(size + 1))  # Cria uma lista de valores de 0 a 1000
    random.shuffle(lista)  # Embaralha a lista de forma aleatória
    # Converte os valores em formato de texto e os junta separados por quebras de linha
    lista_texto = '\n'.join(str(valor) for valor in lista)

    with open('/home/pixies0/UFT/PAA/PAA/src/inputs/' + str(size) + '.txt', 'w') as arquivo:
        arquivo.write(lista_texto)  # Escreve a lista no arquivo de texto

gerar_lista_ordenadaCrescente(10)
gerar_lista_ordenadaDecrescente(10)
gerar_lista_ordenadaAleatoria(10)