numero = int(input("Número a ser repetido: "))
for n in range(numero , 0 , -1):
    print(str(n) * n)
""""
O loop deve começar em N e ir até 1.

Para cada valor i, o programa imprime o número i repetido i vezes.

O uso de range(N, 0, -1) garante a contagem decrescente."""


