ORD_A = ord("A")
ORD_Z = ord("Z")
TAMANHO_ALFABETO = (ORD_Z - ORD_A) + 1


def eh_territorio(territorio):
    """
    Testa se o argumento dado é um território. Um território é representado por um tuplo não nulo
    com A a Z tuplos não nulos, e cada um desses tuplos podem ter desde índice 0 até índice 98.
    Esses índices só podem representar 0 ou 1.

    Args:
        Any, pode ser um argumento de qualquer tipo.

    Returns:
        True, se o argumento for um território válido.
        False, caso contrário.
    """
    if (
        not isinstance(territorio, tuple)#Verificar se é um tuplo e se os caminhos verticais são válidos
        or len(territorio) < 1                 
        or len(territorio) > TAMANHO_ALFABETO
    ):
        return False
    for coluna in territorio:
        if not isinstance(coluna, tuple): #Verificar se dentro do tuplo são tuplos
            return False
        tamanho = len(territorio[0])
        if len(coluna) != tamanho: #Verificar se todos os tuplos têm o mesmo comprimento
            return False
        for intersecao in coluna:
            if intersecao != 1 and intersecao != 0 or not isinstance(intersecao, int):
                return False #Verificar se todos os tuplos são apenas constituídos por números inteiros iguais a 1 ou 0
    if tamanho < 1 or tamanho > 99: #Verificar se os caminhos horizontais são válidos
        return False
    return True


def obtem_ultima_intersecao(territorio):
    """
    Obtém a coordenada da última interseção de um dado território. As interseções são representadas
    por 0 e 1, e estão dentro dos tuplos que representam os caminhos verticais, todos estes dentro
    do tuplo principal.

    Args:
        "territorio": o território a ser analisado.

    Returns:
        Um tuplo com as coordenadas da última interseção.
    """
    indice_coluna = len(territorio) - 1 #Obter a coluna da última interseção
    ultima_coluna = territorio[indice_coluna] #Obter a linha da última interseção
    return (chr(ORD_A + indice_coluna), len(ultima_coluna))


def eh_intersecao(intersecao):
    """
    Testa se o argumento dado é uma interseção, a partir da sua coordenada. é uma coordenada de uma
    interseção se for um tuplo de tamanho 2, onde o primeiro elemento é uma string, com uma letra de
    'A' a 'Z', que representa o caminho vertical, e o segundo elemento é um número de 1 a 99, que
    representa o caminho horizontal.

    Args:
        Any, pode ser um argumento de qualquer tipo.

    Returns:
        True, se o argumento for uma interseção válida.
        False, caso contrário.
    """
    if (
        isinstance(intersecao, tuple) #Tem que ser um tuplo
        and len(intersecao) == 2 #Tem que ter apenas 2 elementos
        and isinstance(intersecao[0], str) #Primeiro elemento é uma string
        and len(intersecao[0]) == 1 #A string tem comprimeiro = 1
        and ord(intersecao[0]) <= ORD_Z 
        and ord(intersecao[0]) >= ORD_A #Só pode ir de 'A' a 'Z'
        and isinstance(intersecao[1], int) #Segundo elemento é um número inteiro
        and intersecao[1] <= 99
        and intersecao[1] > 0 #Só pode ir de 1 a 99
    ):
        return True
    return False


def eh_intersecao_valida(territorio, intersecao):
    """
    Testa se a interseção dada é uma intersecao válida tendo em conta o território dado. Uma interseção
    é válida se o territorio contem o caminho vertical e horizontal nela representados.

    Args:
        Any, pode ser um argumento de qualquer tipo.

    Returns:
        True, se o argumento for uma interseção válida.
        False, caso contrário.
    """
    if not eh_territorio(territorio) or not eh_intersecao(intersecao): #Validação dos argumentos
        return False
    ultima_intersecao = obtem_ultima_intersecao(territorio)
    return (
        ord(intersecao[0]) <= ord(ultima_intersecao[0])
        and intersecao[1] <= ultima_intersecao[1] #Verificar se os limites da interseção dada estão 
    ) #entre a primeira interseção e a última interseção.


def eh_intersecao_livre(territorio, intersecao):
    """
    Testa se a intersecao dada é uma intersecao livre. Cada interseção é representada ou
    pelo número 1 ou pelo número 0. Se for representada pelo número 0 é uma interseção livre, se for
    representada pelo número 1 contém uma montanha.

    Args:
        Any, pode ser um argumento de qualquer tipo.

    Returns:
        True, se o argumento for uma interseção válida.
        False, caso contrário.
    """
    indice_coluna = ord(intersecao[0]) - ORD_A 
    coluna = territorio[indice_coluna]
    return coluna[intersecao[1] - 1] == 0 #Verificar se a interseção no território admite o valor 0 ou 1


def obtem_intersecoes_adjacentes(territorio, intersecao):
    """
    Obtem todas as coordenadas das interseções adjacentes à interseção dada, com base no território dado.
    Estas interseções são devolvidas num tuplo.

    Args:
        Any, pode ser um argumento de qualquer tipo.

    Returns:
        Um tuplo que consiste em todas as coordenadas das interseções adjacentes da interseção dada.
    """
    intersecoes_adjacentes = ()
    indice_coluna = ord(intersecao[0]) - ORD_A
    linha = intersecao[1]
    if linha >= 2: #Impede de adicionar a interseção abaixo se a interseçao dada estiver na linha 1
        intersecoes_adjacentes += ((intersecao[0], linha - 1),) 
    if indice_coluna >= 1: #Impede de adicionar a interseção à esquerda se a interseção dada estiver na coluna 'A'
        intersecoes_adjacentes += ((chr(ord(intersecao[0]) - 1), linha),)
    if indice_coluna < len(territorio) - 1: #Impede de adicionar a interseção à esquerda se a interseção dada estiver na última coluna
        intersecoes_adjacentes += ((chr(ord(intersecao[0]) + 1), linha),)
    primeira_coluna = territorio[0]
    if linha < len(primeira_coluna): #Impede de adicionar a interseção em cima se a interseção dada estiver na última linha
        intersecoes_adjacentes += ((intersecao[0], linha + 1),)
    return intersecoes_adjacentes


def ordena_intersecoes(conjunto_intersecoes):
    """
    Ordena o conjunto de interseções dado com base na leitura. A ordem de leitura
    começa na primeira linha e vai da esquerda para a direita, ou seja, agrupa todas as interseções com
    o mesmo caminho horizontal e ordena com base nos caminhos verticais.

    Args:
        Um tuplo constituido por várias coordenadas de interseções.

    Returns:
        Um tuplo que contém as mesmas interseções, mas ordenadas.
    """
    intersecoes_linhas_ordenadas = ()
    intersecoes_colunas_ordenadas = ()
    linha = 1
    coluna_maxima = linha_maxima = 0
    coluna = ORD_A
    for intersecao in conjunto_intersecoes: #Obtém os limites do território
        if ord(intersecao[0]) > coluna_maxima:
            coluna_maxima = ord(intersecao[0])
        if intersecao[1] > linha_maxima:
            linha_maxima = intersecao[1]
    while linha <= linha_maxima:
        tuplo_linha = ()
        for intersecao in conjunto_intersecoes:
            if intersecao[1] == linha:
                tuplo_linha += (intersecao,)
        intersecoes_linhas_ordenadas += (tuplo_linha,) #Cria um tuplo para cada linha diferente do território
        linha += 1
    for tuplo_linha in intersecoes_linhas_ordenadas:
        coluna = ORD_A
        while coluna <= coluna_maxima: #Para cada tuplo de uma linha, adiciona ao tuplo final pela ordem das letras
            for intersecao in tuplo_linha:
                if ord(intersecao[0]) == coluna:
                    intersecoes_colunas_ordenadas += (intersecao,) 
            coluna += 1 
    return intersecoes_colunas_ordenadas


def territorio_para_str(territorio):
    """
    Transforma o território dado, que está em forma de tuplo, numa string, que representa visualmente
    as interseções, livres ou montanhas e mostra a designação de todos os caminhos verticas e horizontais.

    Args:
        Um tuplo que representa um território.

    Returns:
        Uma string que representa visualmente o território.

    Raises:
        <ValueError>: Caso o argumento dado não seja um território válido.
    """
    if not eh_territorio(territorio):
        raise ValueError("territorio_para_str: argumento invalido")
    ultima_intersecao = obtem_ultima_intersecao(territorio)
    linha_maxima = ultima_intersecao[1]

    def lista_letras(): #Função para escrever as letras da string, já que se usa duas vezes.
        letra = ORD_A
        letras_str = ""
        while letra <= ord(ultima_intersecao[0]):
            letras_str += f" {chr(letra)}"
            letra += 1
        return letras_str

    territorio_str = "  " + lista_letras()
    territorio_str += "\n"
    while linha_maxima >= 1: #Adiciona o número da linha no início
        if linha_maxima < 10: #Se o número tiver 2 dígitos terá de ter um espaço a menos
            territorio_str += " "
        territorio_str += f"{linha_maxima}"
        for coluna in territorio:
            if coluna[linha_maxima - 1] == 0: #Adiciona . se for interseção livre
                territorio_str += " ." 
            else: #Adiciona X se for montanha
                territorio_str += " X"
        if linha_maxima < 10: #Adiciona o número da linha no final
            territorio_str += " "
        territorio_str += f" {linha_maxima}"
        territorio_str += "\n"
        linha_maxima -= 1
    territorio_str += "  " + lista_letras()
    return territorio_str

def obtem_cadeia(territorio, intersecao):
    """
    Obtem a cadeia associada à interseção dada de um certo território dado. Uma cadeia é todas as
    interseções do mesmo tipo (ou todas livres ou todas montanhas) que estão ligadas entre si, ou
    seja, não pode haver uma interseção de outro tipo entre elas.

    Args:
        Um tuplo que representa um território.
        Um tuplo que representa uma interseção.

    Returns:
        Um tuplo que contém todas as coordenadas das interseções que fazem parte da cadeia associada
        à interseção dada

    Raises:
        <ValueError>: Caso os argumentos dados não sejam um território válido ou uma interseção válida.
    """
    if not eh_territorio(territorio) or not eh_intersecao_valida(
        territorio, intersecao #Validação dos argumentos
    ):
        raise ValueError("obtem_cadeia: argumentos invalidos")
    resultado = cadeia = (intersecao,)
    valor_booleano = eh_intersecao_livre(territorio, intersecao) #Verifica se a interseção dada é livre ou uma montanha

    while True:
        cadeia_temporaria = ()
        for intersecao_cadeia in cadeia: #Em cada ciclo vai estar a analisar interseções diferentes (Adjacente das adjacentes)
            adjacentes = obtem_intersecoes_adjacentes(territorio, intersecao_cadeia)
            for adjacente in adjacentes:
                if (
                    eh_intersecao_livre(territorio, adjacente) == valor_booleano
                    and adjacente not in resultado #Não adiciona repetidos
                ):
                    resultado += (adjacente,)
                    cadeia_temporaria += (adjacente,)
        cadeia = cadeia_temporaria
        if len(cadeia) == 0:
            break
    return ordena_intersecoes(resultado)


def obtem_vale(territorio, intersecao):
    """
    Obtem todos os vales associados a uma interseção não livre. Um vale é uma interseção livre que é
    adjacente a uma interseção não livre/ uma cadeia de interseções não livres.

    Args:
        Um tuplo que representa um território.
        Um tuplo que representa uma interseção.

    Returns:
        Um tuplo que contém todas as coordenadas dos vales existentes associados à interseção dada/cadeia
        à qual ela está associada.

    Raises:
        <ValueError>: Caso os argumentos dados não sejam um território válido ou uma interseção válida e a
        interseção seja livre.
    """
    vales = ()
    if ( #Validação dos argumentos
        not eh_territorio(territorio)
        or not eh_intersecao_valida(territorio, intersecao)
        or eh_intersecao_livre(territorio, intersecao)
    ):
        raise ValueError("obtem_vale: argumentos invalidos")
    cadeia = obtem_cadeia(territorio, intersecao)
    for intersecao_cadeia in cadeia: #Obtém as adjacentes da cadeia de montanhas ou da montanha
        adjacentes = obtem_intersecoes_adjacentes(territorio, intersecao_cadeia)
        for adj in adjacentes:
            if eh_intersecao_livre(territorio, adj) and adj not in vales: #Adiciona se for livre e se não estiver no tuplo final
                vales += (adj,)
    return ordena_intersecoes(vales)


def verifica_conexao(territorio, intersecao_a, intersecao_b):
    """
    Verifica se duas interseções estão conectadas. Duas interseções estão conectadas se 1) forem
    do mesmo tipo e 2) todas as interseções entre elas também são do mesmo tipo. Uma maneira fácil
    de se verificar é ver se fazem parte de uma mesma cadeia.

    Args:
        Um tuplo que representa um território.
        Um tuplo que representa uma interseção
        Um tuplo que representa uma interseção

    Returns:
        True, se estiverem conectadas
        False, caso contrário

    Raises:
        <ValueError>: Caso os argumentos dados não sejam um território válido ou interseções válidas.
    """
    if ( #Validação dos argumentos
        not eh_territorio(territorio)
        or not eh_intersecao_valida(territorio, intersecao_a)
        or not eh_intersecao_valida(territorio, intersecao_b)
    ):
        raise ValueError("verifica_conexao: argumentos invalidos")
    cadeia = obtem_cadeia(territorio, intersecao_a) #Se as duas interseções fazem parte da mesma cadeia, estão conectadas
    return intersecao_b in cadeia


def calcula_numero_montanhas(territorio):
    """
    Calcula o número de montanhas existentes num território, ou seja,
    interseções não livres.

    Args:
        Um tuplo que representa um território.

    Returns:
        Um inteiro, que representa o número de montanhas do território.

    Raises:
        <ValueError>: Caso o argumento dado não seja um território válido.
    """
    if not eh_territorio(territorio): #Validação dos argumentos
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    numero_montanhas = 0
    for coluna in territorio:
        for intersecao in coluna:
            if intersecao == 1:
                numero_montanhas += 1 #Percorre o território inteiro, se for um 1 aumenta o número de montanhas dado no final
    return numero_montanhas


def obtem_todas_as_cadeias(territorio): #Função extra
    """
    Obtém todas as cadeias de montanhas existentes num território, ou seja, cadeias de
    interseções não livres.

    Args:
        Um tuplo que representa um território.

    Returns:
        Um tuplo que contém todas as cadeias de montanhas do território.

    Raises:
        <ValueError>: Caso o argumento dado não seja um território válido.
    """
    cadeias = ()
    for coluna in range(len(territorio)):
        for intersecao in range(len(territorio[coluna])):
            if territorio[coluna][intersecao] == 1: #Apenas calcula a cadeia se for uma montanha
                intersecao_ja_processada = False
                for elemento in cadeias: #Se esta interseção já está no tuplo final, não é preciso obter a sua cadeia
                    if ((chr(coluna + 65)), intersecao + 1) in elemento:
                        intersecao_ja_processada = True
                        break
                if intersecao_ja_processada == False: #Se não estiver no tuplo final, calcula-se a sua cadeia.
                    sub_cadeia = obtem_cadeia(territorio, ((chr(coluna + 65)), intersecao + 1))  
                    cadeias += (sub_cadeia, )
    return cadeias
def calcula_numero_cadeias_montanhas(territorio):
    """
    Calcula o número de cadeias de montanhas existentes num território, ou seja, cadeias de
    interseções não livres.

    Args:
        Um tuplo que representa um território.

    Returns:
        Um inteiro, que representa o número de cadeias de montanhas do território.

    Raises:
        <ValueError>: Caso o argumento dado não seja um território válido.
    """
    if not eh_territorio(territorio):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    return len(obtem_todas_as_cadeias(territorio)) #Calcula o comprimeto do tuplo que contém todas as cadeias

def calcula_tamanho_vales(territorio):
    """
    Calcula o número de vales existentes num dado território, ou seja, interseções 
    livres adjacentes a interseções/cadeias de interseções não livres.

    Args:
        Um tuplo que representa um território.
  
    Returns:
        Um inteiro, que representa o número de vales do território.
    Raises:
        <ValueError>: Caso o argumento dado não seja um território válido.
    """
    if not eh_territorio(territorio): #Validar os argumentos
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    resultado_vales = ()
    todas_cadeias = obtem_todas_as_cadeias(territorio)
    for cadeia in todas_cadeias: #Apenas se calcula os vales da primeira interseção de cada cadeia, pois a 
        primeira_intersecao_cadeia = cadeia[0] #função obtem_vale calcula vales de cadeias associadas a interseções
        vales = obtem_vale(territorio, primeira_intersecao_cadeia) 
        for vale in vales:
            if vale not in resultado_vales: #Apenas adiciona se ainda não está no resultado
                    resultado_vales += (vale,)
    return len(resultado_vales)
