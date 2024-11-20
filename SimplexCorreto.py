import copy

def inversa(A):
    linha = len(A)
    col = len(A[0])
    inversa = copy.deepcopy(A)
    for i in range(linha):
        inversa[i] += [1 if i == j else 0 for j in range(linha)]
    inversa = escalonamento(inversa)
    inversa = escalonamento_contrario(inversa)
    col *= 2
    for i in range(linha):
        inversa[i] = inversa[i][col//2:]
    return inversa

def troca_linha(A, pivo):
    linha, col = len(A), len(A[0])
    for i in range(pivo + 1, linha):
        if A[i][pivo] != 0:
            # Trocando as linhas
            A[i], A[pivo] = A[pivo], A[i]
            return True
    return False

def escalonamento(A):
    linha, col = len(A), len(A[0])
    for pivo in range(linha):
        if A[pivo][pivo] == 0:
            if not troca_linha(A, pivo):
                raise ValueError("Matriz não é inversível.")
        # Normalizando o pivô
        pivo_valor = A[pivo][pivo]
        for j in range(col):
            A[pivo][j] /= pivo_valor
        # Zerando os elementos abaixo do pivô
        for i in range(pivo + 1, linha):
            m = A[i][pivo]
            for j in range(col):
                A[i][j] -= m * A[pivo][j]
    return A

def escalonamento_contrario(A):
    linha, col = len(A), len(A[0])
    for pivo in range(linha - 1, -1, -1):
        # Zerando os elementos acima do pivô
        for i in range(pivo - 1, -1, -1):
            m = A[i][pivo]
            for j in range(col):
                A[i][j] -= m * A[pivo][j]
    return A

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
    quantidade_de_restricoes = len(A)
    quantidade_de_variaveis = len(A[0])

    num_de_variaveis_nao_basicas = quantidade_de_variaveis - quantidade_de_restricoes  # n - m
    index_nao_basicas = []
    index_basicas = []

    vetor_x = [0 for _ in range(quantidade_de_variaveis)]  # Inicializa o vetor x com zeros

    # Inicializando os índices das variáveis básicas e não básicas
    for i in range(num_de_variaveis_nao_basicas):
        index_nao_basicas.append(i)

    for i in range(num_de_variaveis_nao_basicas, quantidade_de_variaveis):
        index_basicas.append(i)

    print("vetor x", vetor_x)
    print("index nao basicas", index_nao_basicas)
    print("index basicas", index_basicas)
    print("Variáveis básicas iniciais:", index_basicas)

    while True:
        # Obtendo a solução básica atual
        Xb = obter_Xb(vetor_x, index_basicas)
        try:
            sol_basica = solucao_basica(index_nao_basicas, index_basicas, Xb, b)
        except ValueError as e:
            print(e)
            break

        # Calculando os custos reduzidos
        func_obj = achar_nova_func_obj(cT, index_nao_basicas, index_basicas, A, b)

        print("Custos reduzidos:", func_obj)

        # Verifica se todos os custos reduzidos são não negativos
        if all(c >= 0 for c in func_obj):
            print("Solução ótima encontrada!")
            print("Solução básica ótima Xb:", sol_basica)
            valor_funcao_objetivo = sum(cT[index_basicas[i]] * sol_basica[i] for i in range(len(index_basicas)))
            print("Valor da função objetivo na última iteração:", valor_funcao_objetivo)
            break

        # Escolhendo a variável que entra na base
        valor_que_entra_na_base = entra_base(func_obj)  # A função entra_base deve usar os custos reduzidos
        ax_para_teste = pegar_coluna(A, index_nao_basicas[valor_que_entra_na_base])
        try:
            index_sair_base_nt = teste_da_razao(ax_para_teste, sol_basica)
        except ValueError:
            print("Problema ilimitado detectado!")
            break

        index_sair_base = index_basicas[index_sair_base_nt]

        # Atualizando o índice da variável que entra na base
        index_basicas[index_sair_base_nt] = index_nao_basicas[valor_que_entra_na_base]
        index_nao_basicas[valor_que_entra_na_base] = index_sair_base

        # Deixando tudo em ordem
        index_basicas.sort()
        index_nao_basicas.sort()

        # Atualizando vetor_x com nova solução
        vetor_x = [0 for _ in range(quantidade_de_variaveis)]
        for i in range(len(index_basicas)):
            vetor_x[index_basicas[i]] = sol_basica[i]

        print("Novo vetor x", vetor_x)
        print("Novas index nao basicas", index_nao_basicas)
        print("Novas index basicas", index_basicas)


# Simulação
# A = [
#     [0.5, 0.3, 1, 0, 0],
#     [0.1, 0.2, 0, 1, 0],
#     [0.4, 0.5, 0, 0, 1]
# ]

# b = [3, 1, 3]
# cT = [-3, -2, 0, 0, 0]

# controlador_simplex(A, b, cT)

A = [
    [1, 1, 1, 0],
    [4, 7, 0, 1]
]

b=[5, 28]
cT=[5, 6, 0, 0]

controlador_simplex(A, b, cT)
