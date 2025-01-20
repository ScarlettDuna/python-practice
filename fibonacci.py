# Escribe los primeros 50 números de la serie de Fibonacci
fibonacci = [0, 1]
for i in range(49):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)

