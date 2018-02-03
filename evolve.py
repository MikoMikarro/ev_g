import string
from string import split
import random
import matplotlib.pyplot as plt

file_name = "data.txt"

while True:
        num_gen = input("Numero de alelos: ")
        pob_gen = input("Poblacion inicial de cada alelo: ")
        gener = input("Cantas xeracions: ")
        break
def iniciador(n_gen,p_gen):
    text = ""
    for i  in range(n_gen):
        text += str(i+1)+":"+str(p_gen)+","
    text += "\n"
    file = open(file_name, "w")
    file.write(text)
    file.close()

def evolve():
    file = open(file_name, "r")
    data = file.readlines()[-1]
    file.close()
    new_list = []
    for i in split(data,",")[:-1]:
        for h in range(int(split(i,":")[1])):
            new_list.append(split(i,":")[0])
    pobl = len(new_list)
    new_ind = []
    for i in range(pobl):
        new_ind.append(new_list[int(random.randint(0,pobl-1))])
    file = open(file_name,"r")
    act_data = file.read()
    file.close()
    np_gen = []
    for i in range(num_gen):
        np_gen.append(new_ind.count(str(int(i)+1)))
    text = ""
    for i in range(num_gen):
        text += str(int(i)+1) +":"+ str(np_gen[i])+","
    text += "\n"
    file = open(file_name,"w")
    file.write(act_data+text)
    file.close()
def represent():
    file = open(file_name,"r")
    data = file.readlines()[:-1]
    file.close()
    n_data = []
    for i in data:
        for h in split(i,".")[:-1]:
            n_data.append(h)
    gen_size = len(data)
    populations = []
    for i in range(num_gen):
        populations.append([])
    for i in range(gen_size):
        for l in range(num_gen):
            popgen = 0
            for h in n_data[num_gen*pob_gen*i:(num_gen*pob_gen*i)+(num_gen*pob_gen)]:
                if str(h) == str(int(l)+1):
                    popgen+=1
            populations[l].append(popgen)
    num = 1
    for i in populations:
        num+=1
        plt.plot(range(gen_size),i,label = num)
    plt.show()
iniciador(num_gen,pob_gen)
for i in range(gener):
    evolve()

# check = True
# while check:
#     for i in range(gener):
#         evolve()
#     represent()
#     re_check = True
#     while re_check:
#         print (" Que queres fascer: ")
#         print (" a - anhadir mais generacions")
#         print (" b - sair")
#
#         ans = raw_input()
#
#         if ans.lower() == "a" :
#             while True:
#                 print "Cantas xeracions"
#                 try:
#                     gener = input()
#                     re_check = False
#                     break
#                 except:
#                     print "Numero enteiro"
#         elif ans.lower() == "b":
#             file = file.open(file_name,"w")
#             file.close()
#             check = False
#             break
