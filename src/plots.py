import numpy as np
import matplotlib.pyplot as plt

INPUT_SIZES = [1000,10000,100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
ALGORITHMS = ["bubble","insert", "merge", "quick", "select", "counting", "shell", "radix"]
ALGORITHMS_TITLES = {"bubble": "bubble","insert": "insert", "merge": "merge", "quick":"quick", "select":"select", "counting":"counting", "shell":"shell", "radix":"radix"}
MARKERS = {"bubble":"$B$","insert": "$I$", "merge":"$M$", "quick":"$Q$", "select":"$S$", "counting":"$C$", "shell":"$X$", "radix":"$R$"}

def showAll(ordem):
    try:
        ordenacao = ordem
    except:
        ordenacao = ""

    fig, axs = plt.subplots(2)

    for algorithm in ALGORITHMS:

        tempos = []
        comparacoes = []

        for size in INPUT_SIZES:
            filename = algorithm+" n"+str(size)+ordenacao
            with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+algorithm+"/"+filename) as file:
                dados = list(zip(*(line.strip("").split('\t') for line in file)))
            tempos.append(np.mean(list(map(lambda x: float(x[:-1]), dados[0]))))
            comparacoes.append(np.mean(list(map(lambda x: float(x[:-1]), dados[1]))))

        axs[0].plot(INPUT_SIZES, tempos, marker=MARKERS[algorithm])
        axs[1].plot(INPUT_SIZES, comparacoes,marker=MARKERS[algorithm])

    axs[0].set_xlabel('Tamanho N da entrada')
    axs[0].set_ylabel('Tempo(s)')
    axs[0].set_xscale('log')
    axs[0].set_yscale('log')
    axs[0].legend()

    axs[1].set_xlabel('Tamanho N da entrada')
    axs[1].set_ylabel('Comparações')
    axs[1].set_xscale('log')
    axs[1].set_yscale('log')
    axs[1].legend()

    plt.show()
    
def showUnique(ordem, algorithm):
    try:
        ordenacao = ordem
    except:
        ordenacao = ""

    fig, axs = plt.subplots(2)
    tempos = []
    comparacoes = []
    
    for size in INPUT_SIZES:
        filename = algorithm+" n"+str(size)+ordenacao
        with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+algorithm+"/"+filename) as file:
            dados = list(zip(*(line.strip("").split('\t') for line in file)))
        tempos.append(np.mean(list(map(lambda x: float(x[:-1]), dados[0]))))
        comparacoes.append(np.mean(list(map(lambda x: float(x[:-1]), dados[1]))))
    axs[0].plot(INPUT_SIZES, tempos,label=ALGORITHMS_TITLES[algorithm], marker=MARKERS[algorithm])
    axs[1].plot(INPUT_SIZES, comparacoes, label=ALGORITHMS_TITLES[algorithm], marker=MARKERS[algorithm])

    axs[0].set_xlabel('Tamanho N da entrada')
    axs[0].set_ylabel('Tempo(s)')
    axs[0].set_xscale('log')
    axs[0].set_yscale('log')
    axs[0].legend()

    axs[1].set_xlabel('Tamanho N da entrada')
    axs[1].set_ylabel('Comparações')
    axs[1].set_xscale('log')
    axs[1].set_yscale('log')
    axs[1].legend()

    plt.show()

