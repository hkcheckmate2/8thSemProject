import HRITVIK as paths
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math
# if using a Jupyter notebook, inlcude:
root2pi = (math.pi)**0.5

def probGauss(x,mu,sigma):
	ans = (math.e)**(-0.5*((x-mu)/sigma)**2)
	return ans

print(probGauss(490,336,60))