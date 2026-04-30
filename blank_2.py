import math

G = 6.674 * 1e-11
elek = 1.602 * 1e-19
me = 9.10938 * 1e-31
eps_0 = 8.854 * 1e-12
d = 1e-2


print(1/(4*math.pi * eps_0) * elek**2 / d**2)
print(G*me**2/d**2)

print(math.sqrt(2)* math.sqrt(1/(4*math.pi * eps_0) * elek**2 / (me * d**3)))