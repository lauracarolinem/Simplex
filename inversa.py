import copy

def inversa(matriz):
    n = len(matriz)
    m = len(matriz[0])
    if n != m:
        raise ValueError("A matriz deve ser quadrada para calcular a inversa.")
    
    # Criar uma matriz estendida [A|I]
    matriz_inversa = copy.deepcopy(matriz)
    identidade = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        matriz_inversa[i] += identidade[i]
    
    # Eliminação Gaussiana
    for i in range(n):
        # Verifica se o pivô é zero, troca de linha se necessário
        if matriz_inversa[i][i] == 0:
            for j in range(i + 1, n):
                if matriz_inversa[j][i] != 0:
                    matriz_inversa[i], matriz_inversa[j] = matriz_inversa[j], matriz_inversa[i]
                    break
        
        # Normaliza a linha do pivô
        pivo = matriz_inversa[i][i]
        if pivo == 0:
            raise ValueError("A matriz não é inversível.")
        
        for j in range(2 * n):
            matriz_inversa[i][j] /= pivo
        
        # Elimina os outros elementos na coluna do pivô
        for k in range(n):
            if k != i:
                fator = matriz_inversa[k][i]
                for j in range(2 * n):
                    matriz_inversa[k][j] -= fator * matriz_inversa[i][j]
    
    # Extrai a inversa da matriz estendida
    for i in range(n):
        matriz_inversa[i] = matriz_inversa[i][n:]
    
    return matriz_inversa

# Exemplo de uso
A = [
    [4, 7],
    [2, 6]
]

inv_A = inversa(A)
for linha in inv_A:
    print(linha)
