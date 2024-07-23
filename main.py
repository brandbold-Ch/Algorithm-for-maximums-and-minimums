import random


# Definir la función de evaluación
def evaluate(x):
    return x**3 + 3*x**2 + 1


# Generar una población inicial de tamaño n dentro del rango especificado
def generate_population(size, bounds):
    population = []
    for _ in range(size):
        individual = random.uniform(bounds[0], bounds[1])
        population.append(individual)
    return population


# Selección por torneo
def select_parents(population, fitness, k=3):
    selected = []
    for _ in range(len(population)):
        # Si la población es menor que k, seleccionamos todos los individuos
        if len(population) < k:
            selected.append(random.choice(population))
        else:
            tournament = random.sample(list(zip(population, fitness)), k)
            selected.append(max(tournament, key=lambda ind: ind[1])[0])
    return selected


# Crossover de un punto
def crossover(parent1, parent2):
    return (parent1 + parent2) / 2


# Mutación
def mutate(individual, bounds, mutation_rate):
    if random.random() < mutation_rate:
        return individual + random.uniform(-1, 1) * (bounds[1] - bounds[0]) * 0.1
    return individual


# Crear una nueva generación
def create_new_generation(population, fitness, bounds, mutation_rate):
    new_population = []
    parents = select_parents(population, fitness)
    for i in range(0, len(parents), 2):
        parent1, parent2 = parents[i], parents[i + 1 if i + 1 < len(parents) else 0]
        child = crossover(parent1, parent2)
        child = mutate(child, bounds, mutation_rate)
        new_population.append(child)
    return new_population


# Algoritmo Genético
def genetic_algorithm(bounds, population_size=20, generations=100, mutation_rate=0.01):
    population = generate_population(population_size, bounds)
    for _ in range(generations):
        fitness = [evaluate(ind) for ind in population]
        population = create_new_generation(population, fitness, bounds, mutation_rate)
    return population


# Parámetros para el rango de búsqueda de x
bounds_x = (0, -5)  # Rango de búsqueda específico de 0 a -5
population_size = 20
generations = 100
mutation_rate = 0.01

# Ejecutar el Algoritmo Genético para el rango de búsqueda de x
final_population_x = genetic_algorithm(bounds_x, population_size, generations, mutation_rate)

# Encontrar el mejor y peor individuo para el rango de búsqueda de x
best_individual_x = max(final_population_x, key=evaluate)
max_y_x = evaluate(best_individual_x)
print(f"Maximo valor en el rango de 0 a -5 (eje x): {max_y_x} en x={best_individual_x}")

worst_individual_x = min(final_population_x, key=evaluate)
min_y_x = evaluate(worst_individual_x)
print(f"Minimo valor en el rango de 0 a -5 (eje x): {min_y_x} en x={worst_individual_x}")

print()

# Parámetros para el rango de búsqueda de y
bounds_y = (0, 6)  # Rango de búsqueda específico de 0 a 6

# Ejecutar el Algoritmo Genético para el rango de búsqueda de y
final_population_y = genetic_algorithm(bounds_y, population_size, generations, mutation_rate)

# Encontrar el mejor y peor individuo para el rango de búsqueda de y
best_individual_y = max(final_population_y, key=evaluate)
max_y_y = evaluate(best_individual_y)
print(f"Maximo valor en el rango de 0 a 6 (eje y): {max_y_y} en x={best_individual_y}")

worst_individual_y = min(final_population_y, key=evaluate)
min_y_y = evaluate(worst_individual_y)
print(f"Minimo valor en el rango de 0 a 6 (eje y): {min_y_y} en x={worst_individual_y}")
