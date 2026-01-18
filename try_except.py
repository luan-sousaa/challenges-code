# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input(""))
for i in range(1 , t +1):
  valor = input()
  separado = valor.split()
  a = separado[0]
  b = separado[1]
  try:
    a = int(a)
    b = int(b)
    divisao = a // b
    print(divisao)
  except Exception as e:
    print("Error Code:", e)