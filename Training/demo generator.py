import random

def shuffle(population):
    for n in population:
        i = random.randint(0, len(population) - 1)
        yield population[i]


numbers = [random.randint(1, 10000) for _ in range(100000)]

print(numbers)

for number in shuffle(numbers):
    print(number)