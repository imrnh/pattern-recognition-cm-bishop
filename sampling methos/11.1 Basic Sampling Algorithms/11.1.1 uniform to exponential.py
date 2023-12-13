import numpy as np
import math
import matplotlib.pyplot as plt

def random_uniforms(n=1_000_000, lr = 0, ur=1):
    numbers = []
    for _ in range(n):
        numbers.append(np.random.uniform(lr, ur))

    return numbers


def make_exponential(U, _lambda=1):
    exp_numbers = []
    transformer = lambda u : math.log(u, math.exp(1))
    for u in U:
        exp_numbers.append(transformer(u))

    return exp_numbers


X = random_uniforms(100)
Xexp = make_exponential(X)
print(Xexp)

plt.plot(Xexp)