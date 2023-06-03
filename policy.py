import random
import numpy as np

def policy_set(p):
    p = [random.random() for r in range(len(p))]
    p =[part / sum(p) for part in p]
    return p

def policy_select(p):
    return random.choices([0,1,2,3], k=1, weights=p)[0]

