#Professor, nos tentamos o maximo que conseguimos, mas chegou em um ponto que comecamos a nos confundir 
#Desculpa por nao conseguir entregar o trabalho completo, vamos nos esforcar mais da proxima vez 
#Laura 2211079 e Thiago Gough 2211163

import copy

# result = [x * b for x in a] # PARA MULTIPLICAR ARRAY POR UM CONSTANTE

# FUNCOES NECESSARIAS PARA REALIZAR A INVERSAO DE UMA MATRIZ #

def inversa(A):
    linha = len(A)
    col = len(A[0])
    inversa = copy.deepcopy(A)
    for i in range(linha):
        inversa[i] += [1 if i == j else 0 for j in range(linha)]

    col *= 2

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
  inv = inversa(matriz)
  inv = escalonamento(inv)
  inv = escalonamento_contrario(inv)

  aux = len(inv)
  for rows in range(len(inv)):
    del inv[rows][:aux]

  return inv

# def multiplica_matrizes(A, B):
#   if A is None or B is None:
#         raise ValueError("Uma das matrizes é None.")
#   linhaMatriz1 = len(A)
#   colunaMatriz1 = len(A[0])

#   linhaMatriz2 = len(B)
#   colunaMatriz2 = len(B[0])

#   if colunaMatriz1 != linhaMatriz2:
#         raise ValueError("As matrizes não podem ser multiplicadas. O número de colunas de A deve ser igual ao número de linhas de B.")

#   resultado = []

#   for i in range(linhaMatriz1):
#     resultado.append([])
#     for j in range(colunaMatriz2):
#       listaMult = [x*y for x, y in zip(A[i], [linha[j] for linha in B])]

#       resultado[i].append(sum(listaMult))

#   return resultado

def multiplica_matrizes(A, B):
    # Verifica se algum dos parâmetros é None
    if A is None or B is None:
        raise ValueError("Uma das entradas é None.")

    # Caso B seja um número inteiro, multiplica o array A por esse número
    if isinstance(B, (int, float)):
        return [[x * B for x in linha] for linha in A]

    # Caso A ou B seja um vetor (array 1D), verifica e faz a multiplicação apropriada
    if isinstance(A[0], list):  # A é uma matriz
        linhaMatriz1 = len(A)
        colunaMatriz1 = len(A[0])
    else:  # A é um vetor (array 1D)
        linhaMatriz1 = 1
        colunaMatriz1 = len(A)
        A = [A]  # Converte para lista de listas para facilitar

    if isinstance(B[0], list):  # B é uma matriz
        linhaMatriz2 = len(B)
        colunaMatriz2 = len(B[0])
    else:  # B é um vetor (array 1D)
        linhaMatriz2 = len(B)
        colunaMatriz2 = 1
        B = [[b] for b in B]  # Converte para lista de listas

    # Verifica se as dimensões são compatíveis para multiplicação
    if colunaMatriz1 != linhaMatriz2:
        raise ValueError("As matrizes não podem ser multiplicadas. "
                         "O número de colunas de A deve ser igual ao número de linhas de B.")

    # Cria a matriz resultado
    resultado = [[0 for _ in range(colunaMatriz2)] for _ in range(linhaMatriz1)]

    # Multiplica as matrizes
    for i in range(linhaMatriz1):
        for j in range(colunaMatriz2):
            resultado[i][j] = sum(A[i][k] * B[k][j] for k in range(colunaMatriz1))

    # Se o resultado for um vetor (1 linha), retorna como um vetor 1D
    if linhaMatriz1 == 1:
        return resultado[0]

    return resultado

# Funcao para mostrar matiz #

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
  # print(Xb)
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

# Pegar o B a partir do A para depois inverter e construir solucao geral

def obter_b(A, index_basicas):
  quant_var_base = len(index_basicas)

  B = []

  for i in index_basicas:
    B.append(pegar_coluna(A, i))

  B = transpose(B)

  return B

def solucao_basica(index_nao_basicas, index_basicas, Xb, b):

  # array_ax = [[] for _ in range(len(index_nao_basicas))] # inicializando array que vai conter o array ax de todos as variaveis nao basicas
  array_ax = []
  sol_basica = []

  cont = 0
  B = obter_b(A, index_basicas) # pegando o B
  # mostra_matriz(B)
  B_inv = inversa_completa(B)
  # mostra_matriz(B_inv)

  for i in index_nao_basicas: # Pegando os ax para a resolucao ... parece que ta funcionando
    array_ax.append(pegar_coluna(A, i))

  # Agora vamos pegar todos os componentes necessarios para nossa solucao geral

  # pegando B^-1 * b

  bzin_inversa = multiplica_matrizes(B_inv, b)
    
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
        if ax[i] == 0:
            continue
        else:
            aux.append(value / ax[i])
        
    min_value = min(aux)
    return aux.index(min_value)

# def achar_nova_func_obj(cT, index_nao_basicas, index_basicas, A, b):
    
#     copy_ct = cT
#     B = obter_b(A, index_basicas)
#     B_inv = inversa_completa(B)
    
#     cbt = []
    
#     # Pegando Cb^t
#     for i, valor in enumerate(cT):
#         if valor in index_basicas:
#             cbt.append(valor)
            
#     print(cbt)
    
#     cbtBinv = multiplica_matrizes(cbt, B_inv)
    
#     custos_reduzidos = []
    
#     for j in index_nao_basicas:
#         # Pegamos a coluna da matriz A correspondente à variável não-básica j
#         Aj = pegar_coluna(A, j)
        
#         # Calculamos Cb^T * B^-1 * Aj
#         Cb_Binv_Aj = multiplica_matrizes(cbtBinv, Aj)
        
#         # Custo reduzido: Cj - Cb^T * B^-1 * Aj
#         custo_reduzido = subtract(cT[j], Cb_Binv_Aj)
#         custos_reduzidos.append(custo_reduzido)
        
    
#     print(custos_reduzidos)
#     return custos_reduzidos

def achar_nova_func_obj(cT, index_nao_basicas, index_basicas, A, b):
    # B = Matriz das colunas básicas da matriz A
    B = obter_b(A, index_basicas)
    B_inv = inversa_completa(B)

    # Pegando os custos das variáveis básicas
    cbt = []
    for i in index_basicas:
        cbt.append(cT[i])

    # Multiplicando cB^T * B^-1
    cbtBinv = multiplica_matrizes([cbt], B_inv)  # [cbt] faz cbt ser uma linha única
    
    if isinstance(cbtBinv[0], list):
        cbtBinv = cbtBinv[0]  # Ajusta para trabalhar com um vetor

    custos_reduzidos = []
    
    print("Index não-básicas:", index_nao_basicas)
    
    # Para cada variável não-básica, calculamos seu custo reduzido
    for j in index_nao_basicas:
        # Pegamos a coluna da matriz A correspondente à variável não-básica j
        Aj = pegar_coluna(A, j)
        print(f"Coluna Aj para variável {j}: {Aj}")
        # Calculamos Cb^T * B^-1 * Aj (garantindo que cbtBinv seja uma lista)
        Cb_Binv_Aj = multiplica_matrizes(cbtBinv, [[a] for a in Aj])  # Multiplica matriz por vetor
        print(f"Custo Cb^T * B^-1 * Aj para variável {j}: {Cb_Binv_Aj}")
        
        # Verificar se o resultado é uma lista ou já um valor numérico
        if isinstance(Cb_Binv_Aj, list):
            # Se for uma lista aninhada, extrair o valor
            if isinstance(Cb_Binv_Aj[0], list):
                Cb_Binv_Aj = Cb_Binv_Aj[0][0]
            else:
                Cb_Binv_Aj = Cb_Binv_Aj[0]
        else:
            # Se já for um valor numérico (float), usar diretamente
            Cb_Binv_Aj = Cb_Binv_Aj[0]
            
        # Custo reduzido: Cj - Cb^T * B^-1 * Aj
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

    vetor_x = [i for i in range(quantidade_de_variaveis)]  # Cria um vetor x para facilitar a visualização

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
        Xb = obter_Xb(vetor_x, index_basicas)  # Certifique-se de que obter_Xb utiliza o índice correto
        sol_basica = solucao_basica(index_nao_basicas, index_basicas, Xb, b)

        # Calculando os custos reduzidos
        func_obj = achar_nova_func_obj(cT, index_nao_basicas, index_basicas, A, b)

        print("Custos reduzidos:", func_obj)

        # Verifica se todos os custos reduzidos são não negativos
        if all(c >= 0 for c in func_obj):
            print("Solução ótima encontrada!")
            print("Solução básica ótima Xb:", Xb)
            valor_funcao_objetivo = sum(cT[index_basicas[i]] * sol_basica[i] for i in range(len(index_basicas)))
            print("Valor da função objetivo na última iteração:", valor_funcao_objetivo)
            break

       # Escolhendo a variável que entra na base
        valor_que_entra_na_base = entra_base(func_obj)  # A função entra_base deve usar os custos reduzidos
        ax_para_teste = pegar_coluna(A, valor_que_entra_na_base)
        index_sair_base_nt = teste_da_razao(ax_para_teste, b)
        index_sair_base = index_basicas[index_sair_base_nt]

        # Trocando os valores da base
        index_basicas[index_sair_base_nt] = valor_que_entra_na_base
        index_nao_basicas[valor_que_entra_na_base] = index_sair_base

        # Deixando tudo em ordem
        index_basicas.sort()
        index_nao_basicas.sort()

# Simulação
cont_iteracao = 1

A = [
    [0.5, 0.3, 1, 0, 0],
    [0.1, 0.2, 0, 1, 0],
    [0.4, 0.5, 0, 0, 1]
]

b = [3, 1, 3]
cT = [-3, -2, 0, 0, 0]

controlador_simplex(A, b, cT)