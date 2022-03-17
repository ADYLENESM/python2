import random
random_numbers = random.sample(range(1000), 3)

print("Numeros a sumar", random_numbers)

type(random_numbers)

suma = sum(random_numbers)

print("El resultado de la suma es: ", suma)