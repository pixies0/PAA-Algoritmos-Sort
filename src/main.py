import os
import time
from plots import *
from inputs.gerador_lista import *
from bubble_sort import *
from insert_sort import *
from merge_sort import *
from quick_sort import *
from select_sort import *
from counting_sort import *
from shell_sort import *
from radix_sort import *


def arquivos(numero, ordem):
    list = []

    with open('/home/pixies0/UFT/PAA/PAA/src/inputs/' + str(numero) + str(ordem) + '.txt', 'r') as arq:
        data = arq.read()
        # var = [item.strip() for item in data.split(" ") if item.strip()]
        var = [int(numero) for numero in data.split('\n')]
        
        for i in var:
            if i != ",":
                i = int(i)
                list.append(i)

        arq.close()

    return list

def main():  

    op = 10
    while(op != 0):
        print("0 - Sair")
        print("1 - BubbleSort")
        print("2 - InsertSort")
        print("3 - MergeSort")
        print("4 - QuickSort")
        print("5 - SelectSort")
        print("6 - CountingSort")
        print("7 - ShellSort")
        print("8 - RadixSort")
        print("9 - Plotar comparativos")
        algorithm = int(input("Escolha o seu algoritmo de ordenação: "))
        os.system('clear')
        op = algorithm
    
        if algorithm == 0:
            return
    
        if algorithm == 1:
            nome="bubble"
            tamanho = int(input("Digite o tamanho da entrada: ")) 
            print("1 - Crescente")
            print("2 - Decrescente")
            print("3 - Aleatorio")
            ordem = int(input("Escolha a ordem: "))
            tag = ''
            if(ordem == 1):
                gerar_lista_ordenadaCrescente(tamanho)
                tag = 'ASC'
            elif(ordem == 2):
                gerar_lista_ordenadaDecrescente(tamanho)
                tag = 'DESC'
            elif(ordem == 3):
                gerar_lista_ordenadaAleatoria(tamanho)
                tag = ''
            
            arq = arquivos(tamanho, tag)
            inicio = time.time()  
            comparacao, trocas = bubble_sort(arq)

            tempo_segundos = time.time() - inicio   
            print ("---------------------------------------------------------------------------------------------") 
            print ("tempo: "+str(tempo_segundos)+"s | "+str(comparacao)+" comparacões |" + str(trocas)+ " trocas")
            print ("---------------------------------------------------------------------------------------------") 
            filename=" n"+''.join(str(tamanho) + tag)
            with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+nome+"/"+nome+""+filename, "a") as f:
                f.write("%s\t%s\n" % (tempo_segundos, comparacao))

            showUnique(tag, nome)
            input("Tecle enter para continuar...")
            os.system('clear')

        if algorithm == 2:
            nome="insert"
            tamanho = int(input("Digite o tamanho da entrada: ")) 
            print("1 - Crescente")
            print("2 - Decrescente")
            print("3 - Aleatorio")
            ordem = int(input("Escolha a ordem: "))
            tag = ''
            if(ordem == 1):
                gerar_lista_ordenadaCrescente(tamanho)
                tag = 'ASC'
            elif(ordem == 2):
                gerar_lista_ordenadaDecrescente(tamanho)
                tag = 'DESC'
            elif(ordem == 3):
                gerar_lista_ordenadaAleatoria(tamanho)
                tag = ''
            
            arq = arquivos(tamanho, tag)
            
            inicio = time.time() 
            comparacao, trocas = insert_sort(arq)
            tempo_segundos = time.time() - inicio   
            
            print ("---------------------------------------------------------------------------------------------") 
            print ("tempo: "+str(tempo_segundos)+"s | "+str(comparacao)+" comparacões |" + str(trocas)+ " trocas")
            print ("---------------------------------------------------------------------------------------------") 
            filename=" n"+''.join(str(tamanho) + tag)
            with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+nome+"/"+nome+""+filename, "a") as f:
                f.write("%s\t%s\n" % (tempo_segundos, comparacao))
            
            showUnique(tag, nome)
            input("Tecle enter para continuar...")
            os.system('clear')
            
        if algorithm == 3:
            nome="merge"
            tamanho = int(input("Digite o tamanho da entrada: ")) 
            print("1 - Crescente")
            print("2 - Decrescente")
            print("3 - Aleatorio")
            ordem = int(input("Escolha a ordem: "))
            tag = ''
            if(ordem == 1):
                gerar_lista_ordenadaCrescente(tamanho)
                tag = 'ASC'
            elif(ordem == 2):
                gerar_lista_ordenadaDecrescente(tamanho)
                tag = 'DESC'
            elif(ordem == 3):
                gerar_lista_ordenadaAleatoria(tamanho)
                tag = ''
            
            arq = arquivos(tamanho, tag)
            
            inicio = time.time() 
            comparacao, trocas = merge_sort(arq)
            tempo_segundos = time.time() - inicio   

            print ("---------------------------------------------------------------------------------------------") 
            print ("tempo: "+str(tempo_segundos)+"s | "+str(comparacao)+" comparacões |" + str(trocas)+ " trocas")
            print ("---------------------------------------------------------------------------------------------") 
            filename=" n"+''.join(str(tamanho) + tag)
            with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+nome+"/"+nome+""+filename, "a") as f:
                f.write("%s\t%s\n" % (tempo_segundos, comparacao))
            
            showUnique(tag, nome)
            input("Tecle enter para continuar...")
            os.system('clear')
                  
        if algorithm == 4:
            nome="quick"
            tamanho = int(input("Digite o tamanho da entrada: ")) 
            print("1 - Crescente")
            print("2 - Decrescente")
            print("3 - Aleatorio")
            ordem = int(input("Escolha a ordem: "))
            tag = ''
            if(ordem == 1):
                gerar_lista_ordenadaCrescente(tamanho)
                tag = 'ASC'
            elif(ordem == 2):
                gerar_lista_ordenadaDecrescente(tamanho)
                tag = 'DESC'
            elif(ordem == 3):
                gerar_lista_ordenadaAleatoria(tamanho)
                tag = ''
            
            
            arq = arquivos(tamanho, tag)
            lista = []
            
            for i in arq:
                if i != "," :
                    i = int(i)
                    lista.append(i)
            
            inicio = time.time() 
            comparacao, trocas = quick_sort(arq, 0, len(lista) - 1)
            tempo_segundos = time.time() - inicio   
            
            print ("---------------------------------------------------------------------------------------------") 
            print ("tempo: "+str(tempo_segundos)+"s | "+str(comparacao)+" comparacões |" + str(trocas)+ " trocas")
            print ("---------------------------------------------------------------------------------------------") 
            filename=" n"+''.join(str(tamanho) + tag)
            with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+nome+"/"+nome+""+filename, "a") as f:
                f.write("%s\t%s\n" % (tempo_segundos, comparacao))      
               
            showUnique(tag, nome)
            input("Tecle enter para continuar...")
            os.system('clear')   
                
        if algorithm == 5:
            nome="select"
            tamanho = int(input("Digite o tamanho da entrada: ")) 
            print("1 - Crescente")
            print("2 - Decrescente")
            print("3 - Aleatorio")
            ordem = int(input("Escolha a ordem: "))
            tag = ''
            if(ordem == 1):
                gerar_lista_ordenadaCrescente(tamanho)
                tag = 'ASC'
            elif(ordem == 2):
                gerar_lista_ordenadaDecrescente(tamanho)
                tag = 'DESC'
            elif(ordem == 3):
                gerar_lista_ordenadaAleatoria(tamanho)
                tag = ''
            
            arq = arquivos(tamanho, tag)
            
            inicio = time.time() 
            comparacao, trocas = selection_sort(arq)
            tempo_segundos = time.time() - inicio   

            print ("---------------------------------------------------------------------------------------------") 
            print ("tempo: "+str(tempo_segundos)+"s | "+str(comparacao)+" comparacões |" + str(trocas)+ " trocas")
            print ("---------------------------------------------------------------------------------------------") 
            filename=" n"+''.join(str(tamanho) + tag)
            with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+nome+"/"+nome+""+filename, "a") as f:
                f.write("%s\t%s\n" % (tempo_segundos, comparacao))        
        
            showUnique(tag, nome)
            input("Tecle enter para continuar...")
            os.system('clear')
        
        if algorithm == 6:
            nome="counting"
            tamanho = int(input("Digite o tamanho da entrada: ")) 
            print("1 - Crescente")
            print("2 - Decrescente")
            print("3 - Aleatorio")
            ordem = int(input("Escolha a ordem: "))
            tag = ''
            if(ordem == 1):
                gerar_lista_ordenadaCrescente(tamanho)
                tag = 'ASC'
            elif(ordem == 2):
                gerar_lista_ordenadaDecrescente(tamanho)
                tag = 'DESC'
            elif(ordem == 3):
                gerar_lista_ordenadaAleatoria(tamanho)
                tag = ''
            
            arq = arquivos(tamanho, tag)
            
            inicio = time.time() 
            comparacao, trocas = counting_sort(arq)
            tempo_segundos = time.time() - inicio   

            print ("---------------------------------------------------------------------------------------------") 
            print ("tempo: "+str(tempo_segundos)+"s | "+str(comparacao)+" comparacões |" + str(trocas)+ " trocas")
            print ("---------------------------------------------------------------------------------------------") 
            filename=" n"+''.join(str(tamanho) + tag)
            with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+nome+"/"+nome+""+filename, "a") as f:
                f.write("%s\t%s\n" % (tempo_segundos, comparacao))   
        
            showUnique(tag, nome)
            input("Tecle enter para continuar...")
            os.system('clear')
        
        if algorithm == 7:
            nome="shell"
            tamanho = int(input("Digite o tamanho da entrada: ")) 
            print("1 - Crescente")
            print("2 - Decrescente")
            print("3 - Aleatorio")
            ordem = int(input("Escolha a ordem: "))
            tag = ''
            if(ordem == 1):
                gerar_lista_ordenadaCrescente(tamanho)
                tag = 'ASC'
            elif(ordem == 2):
                gerar_lista_ordenadaDecrescente(tamanho)
                tag = 'DESC'
            elif(ordem == 3):
                gerar_lista_ordenadaAleatoria(tamanho)
                tag = ''
            
            arq = arquivos(tamanho, tag)
            
            inicio = time.time() 
            comparacao, trocas = shell_sort(arq)
            tempo_segundos = time.time() - inicio   

            print ("---------------------------------------------------------------------------------------------") 
            print ("tempo: "+str(tempo_segundos)+"s | "+str(comparacao)+" comparacões |" + str(trocas)+ " trocas")
            print ("---------------------------------------------------------------------------------------------") 
            filename=" n"+''.join(str(tamanho) + tag)
            with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+nome+"/"+nome+""+filename, "a") as f:
                f.write("%s\t%s\n" % (tempo_segundos, comparacao))
                
            showUnique(tag, nome)
            input("Tecle enter para continuar...")
            os.system('clear')
        
        if algorithm == 8:
            nome="radix"
            tamanho = int(input("Digite o tamanho da entrada: ")) 
            print("1 - Crescente")
            print("2 - Decrescente")
            print("3 - Aleatorio")
            ordem = int(input("Escolha a ordem: "))
            tag = ''
            if(ordem == 1):
                gerar_lista_ordenadaCrescente(tamanho)
                tag = 'ASC'
            elif(ordem == 2):
                gerar_lista_ordenadaDecrescente(tamanho)
                tag = 'DESC'
            elif(ordem == 3):
                gerar_lista_ordenadaAleatoria(tamanho)
                tag = ''
            
            arq = arquivos(tamanho, tag)
            
            inicio = time.time() 
            comparacao, trocas = radix_sort(arq)
            tempo_segundos = time.time() - inicio   

            print ("---------------------------------------------------------------------------------------------") 
            print ("tempo: "+str(tempo_segundos)+"s | "+str(comparacao)+" comparacões |" + str(trocas)+ " trocas")
            print ("---------------------------------------------------------------------------------------------") 
            filename=" n"+''.join(str(tamanho) + tag)
            with open("/home/pixies0/UFT/PAA/PAA/src/outputs/"+nome+"/"+nome+""+filename, "a") as f:
                f.write("%s\t%s\n" % (tempo_segundos, comparacao))
                
            showUnique(tag, nome)
            input("Tecle enter para continuar...")
            os.system('clear')
    
        if algorithm == 9:
            print("1 - Crescente")
            print("2 - Decrescente")
            print("3 - Aleatorio")
            ordem = int(input("Escolha a ordem: "))
            tag = ''
            if(ordem == 1):
                tag = 'ASC'
            elif(ordem == 2):
                tag = 'DESC'
            elif(ordem == 3):
                tag = ''
            showAll(tag)
            os.system('clear')
            
        


if __name__ == '__main__':
    main()