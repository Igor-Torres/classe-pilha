import os
import time

class Pilha:
    def __init__(self, nome):
        self.itens = []
        self.nome = nome

    def empilha(self, item):
        self.itens.append(item)

    def desempilha(self):
        if self.itens:
            return self.itens.pop()
        return None

    def topo(self):
        if self.itens:
            return self.itens[-1]
        return None

    def esta_vazia(self):
        return len(self.itens) == 0

    def tamanho(self):
        return len(self.itens)

    def __iter__(self):
        return reversed(self.itens)

    def __str__(self):
        return f"{self.nome}: {self.itens}"

def desenha_pinos(pinos, altura, passo):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Posição Atual: {passo} passos\n")
    
    for nivel in range(altura - 1, -1, -1):
        for pilha in pinos:
            if len(pilha.itens) > nivel:
                disco = pilha.itens[nivel]
                espaco = " " * (altura - disco)
                bloco = "#" * (disco * 2 - 1)
                print(f"{espaco}{bloco}{espaco}", end="\t")
            else:
                print(" " * (altura - 1) + "|" + " " * (altura - 1), end="\t")
        print()
    print("___|___\t___|___\t___|___\n")

def hanoi(n, origem, destino, auxiliar, pinos, altura, M, passo_info):
    if n == 1:
        destino.empilha(origem.desempilha())
        passo_info['contador'] += 1
        if passo_info['contador'] % M == 0 or M == 1:
            desenha_pinos(pinos, altura, passo_info['contador'])
            input("Pressione ENTER para continuar...")
    else:
        hanoi(n - 1, origem, auxiliar, destino, pinos, altura, M, passo_info)
        destino.empilha(origem.desempilha())
        passo_info['contador'] += 1
        if passo_info['contador'] % M == 0 or M == 1:
            desenha_pinos(pinos, altura, passo_info['contador'])
            input("Pressione ENTER para continuar...")
        hanoi(n - 1, auxiliar, destino, origem, pinos, altura, M, passo_info)

def main():
    print("+--------------------------------------------------+")
    print("|         Desafio II - Torre de Hanói             |")
    print("+--------------------------------------------------+\n")

    N = int(input("Digite o número de discos (ex: 3): "))
    M = int(input("Quantos movimentos entre atualizações? (0 = até o fim): "))
    if M == 0:
        M = float('inf')

    origem = Pilha("Origem")
    destino = Pilha("Destino")
    auxiliar = Pilha("Auxiliar")

    for i in range(N, 0, -1):
        origem.empilha(i)

    pinos = [origem, auxiliar, destino]
    passo_info = {'contador': 0}

    desenha_pinos(pinos, N, 0)
    input("Pressione ENTER para iniciar...\n")

    hanoi(N, origem, destino, auxiliar, pinos, N, M, passo_info)

    print(f"\nSolução final em {passo_info['contador']} movimentos.")
    desenha_pinos(pinos, N, passo_info['contador'])

if __name__ == "__main__":
    main()
