import string
from string import split
import random
from random import shuffle
import matplotlib.pyplot as plt

d = "/"

gen = 8
n_alelos = 2
n_individuos_alelo = 5

file_name = "data.txt"

pob = []

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
    for i in split(data,","):
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
    for i in pob_nueva:
        text += str(i) + "."
    text += "\n"
    file = open(file_name,"w")
    file.write(data_prev+text)
    file.close()

#def representar():



iniciar(n_alelos,n_individuos_alelo)
for i in range(gen):
    evolve()
#representar()
