import string
from string import split
import random
import matplotlib.pyplot as plt

file_name = "data.txt"
num_gen = 10
pob_gen = 3000
gener = 200
def iniciador(n_gen,p_gen):
    ind = []
    for i in range(n_gen):
        for l in range(p_gen):
            ind.append(i+1)
    # print ind
    text = ""
    for i in ind:
        text += str(i) + "."
    text += "\n"
    file = open(file_name, "w")
    file.write(text)
    file.close()
def evolve():
    file = open(file_name, "r")
    data = file.readlines()[-1][:-1]
    file.close()

    n_data = []
    for i in split(data,".")[:-1]:
        n_data.append(i)
    pobl = len(n_data)
    new_ind = []
    for i in range(pobl):
        new_ind.append(n_data[int(random.randint(0,pobl-1))])
    file = open(file_name,"r")
    act_data = file.read()
    file.close()
    text = ""
    for i in new_ind:
        text += str(i) + "."
    text += "\n"
    file = open(file_name,"w")
    file.write(act_data+text)
    file.close()

def represent():
    file = open(file_name,"r")
    data = file.readlines()
    file.close()
    n_data = []
    for i in data:
        for h in split(i,".")[:-1]:
            n_data.append(h)
    populations = []
    for i in range(num_gen):
        populations.append([])
    for i in range(gener+1):
        for l in range(num_gen):
            popgen = 0
            for h in n_data[num_gen*pob_gen*i:(num_gen*pob_gen*i)+(num_gen*pob_gen)]:
                if str(h) == str(int(l)+1):

                    popgen+=1
            populations[l].append(popgen)
    num = 1
    for i in populations:
        num+=1
        plt.plot(range(gener+1),i,label = num)
    plt.show()

iniciador(num_gen,pob_gen)
for i in range(gener):
    evolve()
represent()
