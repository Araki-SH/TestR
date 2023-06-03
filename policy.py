import random
import numpy as np

def policy_set(p):
    #random select
    p = [random.random() for r in range(len(p))]
    #sum  add
    p =[part / sum(p) for part in p]
    return p

def policy_select(p):
    #next move select
    return random.choices([0,1,2,3], k=1, weights=p)[0]

