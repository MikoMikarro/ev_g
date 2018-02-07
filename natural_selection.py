import string
from string import split
import random
from random import shuffle
import matplotlib.pyplot as plt

file_name = "data.txt"
ans = ""
pob = []
alelos_ventaja = []

while True:
    n_alelos = input("Alelos:")
    while True:
        n_alelos_ventaxe = input("Alelos con ventaxe evolutiva")
        if n_alelos_ventaxe >= n_alelos:
            print("Un numero aceptable por favor")
        else:
            break
    print "Alelos con vetaja evolutiva: " + str(range(n_alelos_ventaxe))
    n_individuos_alelo = input("Individuos por alelo:")
    generaciones = input("Generaciones:")
    break

def iniciar(n_alelos,n_individuos_alelo):
    for i in range(n_alelos):
        for l in range(n_individuos_alelo):
            pob.append(i+1)

    text = ""
    file = open(file_name,"w")
    for i in range(n_alelos):
        text += str(i+1)+":"+str(n_individuos_alelo)+","
    text += "\n"
    file = open(file_name, "w")
    file.write(text)
    file.close()

def evolve():
    file = open(file_name,"r")
    data = file.readlines()[-1]
    file.close()

    pob_prev = []
    for i in split(data,",")[:-1]:
        for l in range(int(split(i,":")[1])):
            pob_prev.append(split(i,":")[0])

    pob_nueva = []
    n_pob = len(pob_prev)

    for i in range(n_pob):
        dato_nuevo_1 = str(pob_prev[random.randint(0,n_pob-1)])
        dato_nuevo_2 = str(pob_prev[random.randint(0,n_pob-1)])
        check_f = True
        for l in range(n_alelos_ventaxe):
            if str(l) == str(dato_nuevo_1):
                pob_nueva.append(dato_nuevo_1)
                check_f = False
        if check_f == True:
            pob_nueva.append(dato_nuevo_2)

    file = open(file_name,"r")
    data_prev = file.read()
    file.close()
    text = ""
    new_data = []

    for i in range(n_alelos):
        new_data.append(pob_nueva.count(str(int(i)+1)))

    for i in range(n_alelos):
        text += str(int(i)+1) + ":" + str(new_data[i]) + ","

    text += "\n"
    file = open(file_name,"w")
    file.write(data_prev+text)
    file.close()

def representar():
    file = open(file_name,"r")
    data = file.readlines()
    file.close()

    pob_rep = []

    n_generaciones = len(data)

    for i in range(n_alelos):
        pob_rep.append([])

    for i in range(len(data)):
        for l in range(n_alelos):
            if int(split(split(data[i],",")[l],":")[1]) == 0:
                if int(split(split(data[i-1],",")[l],":")[1]) == 0 and i > 0:
                    pass
                else:
                    pob_rep[l].append(int(0))
            else:
                pob_rep[l].append(int(split(split(data[i],",")[l],":")[1]))

    for i in range(len(pob_rep)):
        print range(len(pob_rep[i]))
        print pob_rep[i]
    for i in range(len(pob_rep)):
        plt.plot(range(len(pob_rep[i])),pob_rep[i],".-")

    plt.show()
#---------------------------#
k = 0
iniciar(n_alelos,n_individuos_alelo)
for i in range(generaciones):
    k += 1
    print "Generacion: ",k
    evolve()

representar()

check_1 = True
while check_1:
    print "Opciones:"
    print "A -> Anhadir mas generaciones."
    print "B -> Seguir hasta que solo queden n con vida."
    print "C -> Salir."
    resp = raw_input()

    if resp.upper() == "A" :
        check_2 = True
        while check_2:
            ad_generaciones = input("Numero de generaciones adicionales:")
            for i in range(ad_generaciones):
                k += 1
                print "Generacion: ",k
                evolve();

            representar()
            check_2 = False

    elif resp.upper() == "B" :
        check_3 = True
        while check_3:
            resp_2 = input("Alelos supervivientes:")
            while True:
                if resp_2 <= n_alelos and resp_2 >=1:
                    break
                else:
                    print "Error"
            check_4 = True

            while check_4:
                evolve()
                k += 1
                print "Generacion: ",k
                file = open(file_name,"r")
                data = file.readlines()[-1]
                file.close()
                pob_prev = []
                for i in split(data,",")[:-1]:
                    pob_prev.append(int(split(i,":")[1]))

                n = pob_prev.count(0)
                if n >= n_alelos - resp_2 :
                    representar()
                    check_4 = False
                    check_3 = False
                    break


    elif resp.upper() == "C":
        check_1 = False
        break
