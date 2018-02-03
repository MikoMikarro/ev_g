################### --- Libraries

import string
from string import split
import random
import matplotlib.pyplot as plt

#################### --- Initial values

file_name= "data.txt"
while True:
        num_gen = input("Number of species: ")
        pob_gen = input("Initial Population for each specie: ")
        gener = input("Number of initial generations: ")
        break

################### --- Functions

def iniciador(n_gen,p_gen): # Here we add the initial specimens
    text = ""
    for i  in range(n_gen):
        text += str(i+1)+":"+str(p_gen)+"," #We add first the id of the specie then ":", population and a "," for using the split tool easier
    text += "\n" # Each line is a generations
    file = open(file_name, "w")
    file.write(text) # Storing the data
    file.close()
def evolve(): # Creating the diferences in species population ... (kind of natural selection)
    file = open(file_name, "r")
    data = file.readlines()[-1] # It only evolves from the last generation
    file.close()
    new_list = []
    for i in split(data,",")[:-1]:
        for h in range(int(split(i,":")[1])):
            if int(split(i,":")[0])  != 0:
                new_list.append(split(i,":")[0]) # Creating an list of the suposed specimens should be
    new_ind = []
    for i in range(pob_gen*num_gen):
        new_ind.append(new_list[int(random.randint(0,len(new_list)-1))]) # Natural selection - The species with more specimens have more chances of surviving and killing others to have  more
    file = open(file_name,"r")
    act_data = file.read() # Reading actual data
    file.close()
    np_gen = []
    for i in range(num_gen):
        np_gen.append(new_ind.count(str(int(i)+1)))  # Creating the new population per specie values
    text = ""
    for i in range(num_gen):
        text += str(int(i)+1) +":"+ str(np_gen[i])+"," # Creating the new generation info
    text += "\n"
    file = open(file_name,"w")
    file.write(act_data+text) # Storing it without destroying what we had
    file.close()
def represent(): # It's just for visualicing the evolutions made
    file = open(file_name,"r")
    data = file.readlines() # Taking each generation
    file.close()
    populations = []
    for i in range(num_gen):
        populations.append([])
    gen_size  = len(data)
    for i in data:
        for l in range(num_gen):
            populations[l].append(int(split(split(i,",")[l],":")[1])) #We need to create a list of list, each big list is a reference to each specie and inside there is the evolution of its population
    for i in populations:
        plt.plot(range(gen_size),i, linewidth = 2)  # Creating graph
    plt.show()

############# ---  Menu and init

iniciador(num_gen,pob_gen)

chMenu
while check:
    num = 1
    for i in range(gener):
        evolve()
        print "evolved- ",num
        num+=1
    represent()
    re_check = True
    while re_check:
        print (" Menu: ")
        print (" a - add more generations")
        print (" b - exit")
        print (" c - evolve until 1 is left")
        print (" d - volve until x is left")
        ans = raw_input()
        if ans.lower() == "a" :
            while True:
                print "How many generations:"
                try:
                    gener = input()
                    re_check = False
                    break
                except:
                    print "Entire number"
        elif ans.lower() == "b":
            file = open(file_name,"w")
            file.close()
            check = False
            break
        elif ans.lower() == "c":
            super_check = True
            while super_check:
                evolve()
                print "evolved- ",num
                num+=1
                file = open(file_name,"r")
                data = file.readlines()[-1]
                for i in range(num_gen):
                    if int(split(split(data,",")[i],":")[1]) == (num_gen * pob_gen):
                        represent()
                        super_check = False
                        break
        elif ans.lower() == "d":
            print("How many species do you want to maintain alive")
            super_check = True
            while True:
                passnum_s = input()
                if ans <= num_gen and ans >= 1:
                    break
                else:
                    print "number between 1 and ",num_gen
            while super_check:
                evolve()
                print "evolved- ",num
                num+=1
                file = open(file_name,"r")
                data = file.readlines()[-1]
                num_r = 0

                for i in range(num_gen):
                    if int(split(split(data,",")[i],":")[1]) == 0:
                        num_r += 1
                    if num_r == (num_gen-num_s):
                        represent()
                        super_check = False
                        break
