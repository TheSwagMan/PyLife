import random
import time

def cp_matrix(m):
    r=[]
    for i in range(len(m)):
        r.append([])
        for j in range(len(m[i])):
            r[i].append(m[i][j])
    return r

def bit_random():
    return random.randint(0,1)

def get_date():
    return time.strftime("%Y-%m-%d_%H-%M-%S")