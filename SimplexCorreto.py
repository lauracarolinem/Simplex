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

def troca_linha(A, pivo):
    linha, col = len(A), len(A[0])
    for i in range(pivo + 1, linha):
        if A[i][pivo] != 0:
            # Trocando as linhas
            A[i], A[pivo] = A[pivo], A[i]
            return True
    return False

def escalonamento(A):
    n, m = len(A), len(A[0])
    for pivo in range(n):
        if A[pivo][pivo] == 0:
            for i in range(pivo + 1, n):
                if A[i][pivo] != 0:
                    A[pivo], A[i] = A[i], A[pivo]
                    break
        pivo_valor = A[pivo][pivo]
        if pivo_valor == 0:
            raise ValueError("A matriz não é inversível.")
        for j in range(m):
            A[pivo][j] /= pivo_valor
        for i in range(pivo + 1, n):
            fator = A[i][pivo]
            for j in range(m):
                A[i][j] -= fator * A[pivo][j]

def escalonamento_contrario(A):
    n, m = len(A), len(A[0])
    for pivo in range(n - 1, -1, -1):
        for i in range(pivo - 1, -1, -1):
            fator = A[i][pivo]
            for j in range(m):
                A[i][j] -= fator * A[pivo][j]

def inversa_completa(matriz):
    try:
        inv = inversa(matriz)
        return inv
    except ValueError:
        print("Erro: Matriz não é inversível.")
        return None

def multiplica_matrizes(A, B):
    # Verifica se as dimensões são compatíveis para multiplicação
    if len(A[0]) != len(B):
        raise ValueError("As matrizes não podem ser multiplicadas. O número de colunas de A deve ser igual ao número de linhas de B.")
    
    # Inicializa a matriz resultado com zeros
    resultado = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    # Multiplica as matrizes
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                resultado[i][j] += A[i][k] * B[k][j]
    
    return resultado

def mostra_matriz(mat, mantissa=7, casas=2):
    for linha in mat:
        for elem in linha:
            formatacao = f".{casas}f"
            print(f"{elem:{mantissa}{formatacao}}", end=' ')
        print()

def pegar_coluna(matriz, index_coluna):
    return [row[index_coluna] for row in matriz]

def obter_Xb(x, index_basicas):
    Xb = []
    for i in index_basicas:
        Xb.append(x[i])
    return Xb

def print_list_vertically(lst):
    for item in lst:
        print(item)

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def subtract(arr1, arr2):
    if isinstance(arr1[0], list):  # Matrix case
        return [[a - b for a, b in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
    else:  # Array case
        return [a - b for a, b in zip(arr1, arr2)]

def add(arr1, arr2):
    if isinstance(arr1[0], list):  # Matrix case
        return [[a + b for a, b in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]
    else:  # Array case
        return [a + b for a, b in zip(arr1, arr2)]

def obter_b(A, index_basicas):
    B = []
    for i in index_basicas:
        B.append(pegar_coluna(A, i))
    B = transpose(B)
    return B

def solucao_basica(index_nao_basicas, index_basicas, Xb, b):
    B = obter_b(A, index_basicas)  # Pegando o B
    B_inv = inversa_completa(B)
    if B_inv is None:
        raise ValueError("Erro ao calcular a inversa de B.")
    
    b_coluna = [[bi] for bi in b]  # Transforma `b` em uma matriz coluna
    bzin_inversa = multiplica_matrizes(B_inv, b_coluna)
    
    sol_basica = []
    cont = 0
    for i in range(len(index_nao_basicas) + len(index_basicas)):
        if i in index_basicas:
            sol_basica.append(bzin_inversa[cont][0])
            cont += 1
        else:
            sol_basica.append(0)
    
    print("Solucao Basica: ", sol_basica)
    return sol_basica

def entra_base(cT):
    maior_custo_relativo = min(cT)
    if maior_custo_relativo > 0:
        return False
    return cT.index(maior_custo_relativo)

def teste_da_razao(ax, b):
    aux = []
    for i, value in enumerate(b):
        if i >= len(ax) or ax[i] == 0:
            continue
        else:
            aux.append(value / ax[i])
    
    if not aux:
        raise ValueError("Não foi possível calcular a razão, todos os elementos em ax são zero ou não há correspondentes válidos em b.")
    
    min_value = min(aux)
    return aux.index(min_value)

def achar_nova_func_obj(cT, index_nao_basicas, index_basicas, A, b):
    B = obter_b(A, index_basicas)
    B_inv = inversa_completa(B)
    cbt = [cT[i] for i in index_basicas]
    cbtBinv = multiplica_matrizes([cbt], B_inv)
    cbtBinv = cbtBinv[0]  # Garantir que é uma matriz 1xN

    custos_reduzidos = []
    print("Index não-básicas:", index_nao_basicas)
    for j in index_nao_basicas:
        Aj = pegar_coluna(A, j)
        print(f"Coluna Aj para variável {j}: {Aj}")
        Cb_Binv_Aj = multiplica_matrizes([cbtBinv], [[a] for a in Aj])  # Multiplica matriz por vetor
        print(f"Custo Cb^T * B^-1 * Aj para variável {j}: {Cb_Binv_Aj}")
        
        if isinstance(Cb_Binv_Aj, list):
            if isinstance(Cb_Binv_Aj[0], list):
                Cb_Binv_Aj = Cb_Binv_Aj[0][0]
            else:
                Cb_Binv_Aj = Cb_Binv_Aj[0]
        else:
            Cb_Binv_Aj = Cb_Binv_Aj
        
        custo_reduzido = cT[j] - Cb_Binv_Aj
        print(f"Custo reduzido para variável {j}: {custo_reduzido}")
        custos_reduzidos.append(custo_reduzido)
    return custos_reduzidos

def controlador_simplex(A, b, cT):
    # Adicionar variáveis de folga
    n_restricoes = len(A)
    n_variaveis = len(A[0])
    A = [row + [1 if i == j else 0 for j in range(n_restricoes)] for i, row in enumerate(A)]
    cT = cT + [0] * n_restricoes

    index_basicas = list(range(n_variaveis, n_variaveis + n_restricoes))
    index_nao_basicas = list(range(n_variaveis))

    while True:
        B = [[A[i][j] for j in index_basicas] for i in range(n_restricoes)]
        try:
            B_inv = inversa_completa(B)
        except ValueError:
            print("Matriz B não é inversível. Problema mal formulado.")
            break

        # Imprimir as matrizes B e B_inv para depuração
        # print("Matriz B:")
        # mostra_matriz(B)
        # print("Matriz B^-1:")
        # mostra_matriz(B_inv)

        cb = [cT[j] for j in index_basicas]
        cB_Binv = [sum(cb[i] * B_inv[i][k] for i in range(n_restricoes)) for k in range(n_restricoes)]

        custos_reduzidos = []
        for j in index_nao_basicas:
            Aj = [A[i][j] for i in range(n_restricoes)]
            Aj_binv = [sum(B_inv[i][k] * Aj[k] for k in range(n_restricoes)) for i in range(n_restricoes)]
            custo_reduzido = cT[j] - sum(cB_Binv[i] * Aj_binv[i] for i in range(n_restricoes))
            custos_reduzidos.append(custo_reduzido)

        if all(cr >= 0 for cr in custos_reduzidos):
            print("Solução ótima encontrada!")
            
            # Calculando Xb para as variáveis básicas
            Xb = [sum(B_inv[i][k] * b[k] for k in range(n_restricoes)) for i in range(n_restricoes)]

            # Criando o vetor de solução completo
            solucao = [0] * (n_variaveis + n_restricoes)
            for i, idx in enumerate(index_basicas):
                solucao[idx] = Xb[i]
            
            # Separando as variáveis originais e as de folga
            solucao_originais = solucao[:n_variaveis]
            print("Solução:", solucao)
            print("Valor da função objetivo:", sum(solucao[i] * cT[i] for i in range(n_variaveis)))
            break

        entra = index_nao_basicas[custos_reduzidos.index(min(custos_reduzidos))]
        Aj = [A[i][entra] for i in range(n_restricoes)]
        Aj_binv = [sum(B_inv[i][k] * Aj[k] for k in range(n_restricoes)) for i in range(n_restricoes)]

        if all(ai <= 0 for ai in Aj_binv):
            print("Problema ilimitado.")
            break

        razoes = [b[i] / Aj_binv[i] if Aj_binv[i] > 0 else float('inf') for i in range(n_restricoes)]
        sai = index_basicas[razoes.index(min(razoes))]

        index_basicas[index_basicas.index(sai)] = entra
        index_nao_basicas[index_nao_basicas.index(entra)] = sai

#NAO DEU
# A = [
#     [1, 1, 1],
#     [0, 1, 2],
#     [-1, 2, 2]
# ]

# b = [6, 8, 4]
# cT = [-2, -10, -8]

# controlador_simplex(A, b, cT)

A = [
    [400,300],
    [300,400],
    [200,500]
]

b = [25000,27000,30000]
cT = [-20000,-25000]

controlador_simplex(A, b, cT)
# A = [
#     [2, 1],
#     [1, 1]
# ]

# b = [6,4]
# cT = [-3,-2]

# controlador_simplex(A, b, cT)

# Simulação
# A = [
#     [0.5, 0.3, 1, 0, 0],
#     [0.1, 0.2, 0, 1, 0],
#     [0.4, 0.5, 0, 0, 1]
# ]

# b = [3, 1, 3]
# cT = [-3, -2, 0, 0, 0]

# controlador_simplex(A, b, cT)

# A = [
#     [1, 1],
#     [4, 7]
# ]

# b = [5, 28]
# cT = [-5, -6]

# controlador_simplex(A, b, cT)
