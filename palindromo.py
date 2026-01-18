def valida_palindromo_modificado(s):
    # Função auxiliar simples: verifica se um texto JÁ É palíndromo
    # Ela só inverte e compara
    def eh_palindromo(texto):
        return texto == texto[::-1]

    # 1. Configurar os ponteiros
    esquerda = 0
    direita = len(s) - 1
    
    # 2. Loop enquanto não se cruzarem
    while esquerda < direita:
        
        # Se as letras são iguais, só avança
        if s[esquerda] == s[direita]:
            esquerda += 1
            direita -= 1
        
        # 3. ENCONTROU DIVERGÊNCIA! (Aqui é o pulo do gato)
        else:
            # Opção A: Ignorar a letra da esquerda
            # Pega o texto do índice seguinte até o fim atual
            teste_apagar_esq = s[esquerda + 1 : direita + 1]
            
            # Opção B: Ignorar a letra da direita
            # Pega o texto do início atual até antes do fim
            teste_apagar_dir = s[esquerda : direita]
            
            # Se qualquer um dos dois for palíndromo, deu certo!
            return eh_palindromo(teste_apagar_esq) or eh_palindromo(teste_apagar_dir)
            
    return True # Se passou pelo loop todo sem problemas

# Teste
print(valida_palindromo_modificado("radkar")) # True (Remove o 'k' vira 'radar')
print(valida_palindromo_modificado("abcde"))  # False (Não tem salvação)