import string
from string import split
import random
from random import shuffle
import matplotlib.pyplot as plt

d = "/"

generacion = 8
n_alelos = 5
n_individuos_alelo = 10

file_name = "data.txt"

pob = []

while True:
    n_alelos = input("Alelos:")
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
        pob_nueva.append(pob_prev[random.randint(0,n_pob-1)])

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

    for i in range(n_alelos):
        for h in data:
            for l in split(h,",")[:-1]:
                if split(h,":")[0] == str(i):
                    pob_rep.append(split(h,":")[1])

    print pob_rep

    #
    # for i in range(n_alelos):
    #
    #     # for i in range(n_alelos):
    #     # pob_alelo.append(pob_rep.count(str(int(i)+1)))




    # for i in range(n_alelos):
    #     plt.plot(pob_rep[i+1],)
    #
    # plt.show()


iniciar(n_alelos,n_individuos_alelo)
for i in range(generaciones):
    evolve()
representar()
