def diagonalDifference(arr):
    # 1. Defina variáveis para as duas somas
    soma_principal = 0
    soma_secundaria = 0
    
    # Descobre o tamanho da matriz (N)
    n = len(arr)
    
    # 2. Crie o loop para percorrer as linhas
    for i in range(n):
        # Acessando a diagonal principal: arr[linha][coluna]
        # Dica: Na principal, linha e coluna são iguais
        soma_principal += arr[i][i] 
        
        # Acessando a diagonal secundária
        # Dica: A coluna é calculada de trás pra frente (n - 1 - i)
        soma_secundaria += arr[i][n - 1 - i]
        
    # 3. Retorne a diferença absoluta
    return abs(soma_principal - soma_secundaria)

# Testando (não precisa alterar abaixo)
if __name__ == '__main__':
    matriz_teste = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    resultado = diagonalDifference(matriz_teste)
    print(f"O resultado deve ser 15. Seu código retornou: {resultado}")