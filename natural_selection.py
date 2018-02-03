import string
from string import split
import random
from random import shuffle
import matplotlib.pyplot as plt

d = "/"

gen = 8
n_alelos = 12
n_individuos_alelo = 5

file_name = "data.txt"

def iniciar(n_alelos,n_individuos_alelo):
    pob = []
    for i in range(n_alelos):
        for l in range(n_individuos_alelo):
            pob.append(i+1)

    lines = []
    file = open(file_name,"w")
    text = ""
    for i in pob:
        text += str(i) + "."
    text += "\n"
    file = open(file_name, "w")
    file.write(text)
    file.close()

def evolve():
    file = open(file_name,"r")
    pob_prev = file.readlines()[-1][:-1]
    file.close()
    pob_prev_n = []
    for i in split(pob_prev,".")[:-1]:
        pob_prev_n.append(i)
    n_pob = len(pob_prev_n)
    pob_nueva = []
    for i in range(n_pob):
        pob_nueva.append(pob_prev_n[random.randint(0,n_pob-1)])
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
