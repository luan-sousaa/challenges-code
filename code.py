num = 0
soma = 0
termos = int(input("digite a quantidade de termos:"))
i = 1
for i in range(int(termos)):
    num = num * 10 + 1
    soma = soma + num

print("soma: ", soma)

