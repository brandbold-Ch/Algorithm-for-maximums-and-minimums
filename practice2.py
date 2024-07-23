# Algoritmo para hallar el mínimo de una función

from math import e, cos

function = lambda x: x**2 - 10*x

list_range_x = list(range(-10, 10, 1))
list_range_y = [function(x) for x in range(-10, 10, 1)]

print(list_range_x[int((len(list_range_x) - 1) / 2)])
print(list_range_y[int((len(list_range_y) - 1) / 2)])
