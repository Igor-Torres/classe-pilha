import time

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mudar(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"[{self.x}, {self.y}]"


def mostrar_matriz(matriz, delay=False):
    for linha in matriz:
        visual = linha.replace('1', ' ').replace('0', '#')
        print(visual)
    if delay:
        input("\n[ENTER] para continuar...")


def preenche_com_pilha(matriz, lin, col, marca='0', passos=0):
    pilha = [Ponto(col, lin)]
    contador = 0

    while pilha:
        p = pilha.pop()
        x, y = p.x, p.y

        if matriz[y][x] not in ('1', marca):
            linha_lista = list(matriz[y])
            linha_lista[x] = marca
            matriz[y] = ''.join(linha_lista)

            # Adiciona vizinhos
            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= ny < len(matriz) and 0 <= nx < len(matriz[0]):
                    if matriz[ny][nx] not in ('1', marca):
                        pilha.append(Ponto(nx, ny))

        # Controle de passos
        contador += 1
        if passos > 0 and contador % passos == 0:
            mostrar_matriz(matriz, delay=True)


def encontra_posicao_X(matriz):
    for y, linha in enumerate(matriz):
        for x, caractere in enumerate(linha):
            if caractere == 'X':
                return y, x
    return None, None


def carregar_matriz(arquivo):
    with open(arquivo, 'r') as f:
        return [linha.strip() for linha in f if linha.strip()]


def salvar_matriz(matriz, arquivo_saida):
    with open(arquivo_saida, 'w') as f:
        for linha in matriz:
            f.write(linha + '\n')


def main():
    nome_arquivo = "matriz_exemplo.txt"
    matriz = carregar_matriz(nome_arquivo)

    print("Matriz original:\n")
    mostrar_matriz(matriz)

    lin, col = encontra_posicao_X(matriz)
    if lin is None:
        print("Erro: posição inicial com 'X' não encontrada.")
        return

    # Substitui 'X' por '0' (ponto inicial do preenchimento)
    linha_lista = list(matriz[lin])
    linha_lista[col] = '0'
    matriz[lin] = ''.join(linha_lista)

    try:
        passos = int(input("\nDigite a quantidade de passos por pausa (0 para preencher direto): "))
    except ValueError:
        passos = 0

    print("\nIniciando preenchimento da região...\n")
    preenche_com_pilha(matriz, lin, col, marca='0', passos=passos)

    print("\nMatriz preenchida:\n")
    mostrar_matriz(matriz)

    salvar_matriz(matriz, "matriz_preenchida.txt")
    print("\nMatriz final salva em 'matriz_preenchida.txt'.")


if __name__ == "__main__":
    main()
