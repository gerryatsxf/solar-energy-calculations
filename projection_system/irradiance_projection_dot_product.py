import numpy as np

def dot_product(ALPHA,BETA,A,B):
    return np.cos(ALPHA)*np.sin(BETA)*np.cos(A-B) + np.sin(ALPHA)*np.cos(BETA)

def main(ALPHA,BETA,A,B):
    return dot_product(ALPHA,BETA,A,B)