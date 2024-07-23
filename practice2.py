# Algoritmo para hallar el mínimo de una función

from math import e, cos

function = lambda x: x**2 - 10*x

list_range_x = list(range(-10, 10, 1))
list_range_y = [function(x) for x in range(-10, 10, 1)]
points = list(zip(list_range_x, list_range_y))

#print(list_range_x[int((len(list_range_x) - 1) / 2)])
#print(list_range_y[int((len(list_range_y) - 1) / 2)])

print(list(zip(list_range_x, list_range_y)))

critical_point = [function(x[0]) == x[1] and function(x[1]) != 0 for x in points]
print(critical_point)
