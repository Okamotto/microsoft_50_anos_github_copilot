number = int(input())

def is_prime(n):
    if n < 2:  # Números menores que 2 não são primos
        return False
    for i in range(2, int(n**0.5) + 1):  # Verifica divisores até a raiz quadrada de n
        if n % i == 0:
            return False
    return True

if is_prime(number):
    print(f"{number} é um número primo!")
else:
    print(f"{number} não é um número primo.")