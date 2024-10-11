import random
from names import names

# Lista com 200 nomes para ser ordenada.
print(names)

# Gera uma lista com 1000 números aleatórios entre 0 e 10000
random_numbers = [random.randint(0, 10000) for _ in range(1000)]

# Exibe a lista gerada
print(random_numbers)