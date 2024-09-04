def main():
    pilhas = definir_jogo()
    jogar(pilhas)


def definir_jogo():
    pilhas = []
    npilhas = input("Quantas pilhas são? ")
    for i in range(0, int(npilhas)):
        npalitos = input("Quantos palitos tem a pilha " + str(i+1) + "? ")
        pilhas.append(int(npalitos))
    
    return pilhas


def jogar(pilhas):
    primeiro = int(input("Quem começa? (Digite 1 para o jogador ou 0 para a máquina)"))

    if primeiro == 1:
        movimento_da_pessoa(pilhas)
    while sum(pilhas) > 0:
        pilhas = movimento_da_maquina(pilhas)
        if sum(pilhas) == 0:
            print("A máquina ganhou!")
            break
        pilhas = movimento_da_pessoa(pilhas)
        if sum(pilhas) == 0:
            print("Você ganhou!")
            break


def movimento_da_pessoa(pilhas):
    #separe as pilhas com palitos
    pilhas_com_palitos = []
    for i in range(0, len(pilhas)):
        if pilhas[i] > 0:
            pilhas_com_palitos.append(i+1)
    #escolhe a pilha a se retirar os palitos
    pilha_escolhida = escolhe_pilha(pilhas_com_palitos)

    #escolhe a quantidade de palitos a se retirar
    npalitos = escolhe_palitos(pilhas, pilha_escolhida)
    
    
    pilhas[pilha_escolhida] = pilhas[pilha_escolhida] - npalitos
    
    print("Você tirou palitos. As pilhas agora são: " + str(pilhas))

    return pilhas

def escolhe_pilha(pilhas_com_palitos):
    pilha = int(input("De qual pilha você quer tirar palitos? Escolha entre " + str(pilhas_com_palitos)+ ": "))
    if pilha not in pilhas_com_palitos:
        print("Essa pilha não tem palitos")
        return escolhe_pilha(pilhas_com_palitos)
    else:
        return pilha - 1

def escolhe_palitos(pilhas, pilha_escolhida):
    palitos = int(input("Quantos palitos você quer tirar? "))
    if palitos > pilhas[pilha_escolhida]:
        print("Essa pilha não tem tantos palitos")
        return escolhe_palitos(pilhas, pilha_escolhida)
    elif palitos < 1:
        print("Você deve tirar pelo menos um palito")
        return escolhe_palitos(pilhas, pilha_escolhida)
    else: 
        return palitos

def movimento_da_maquina(pilhas):
    NimSum = 0
    pilha_com_palitos = 0
    for i in range(0, len(pilhas)):
        NimSum = NimSum ^ pilhas[i]
        if pilhas[i] > 0:
            pilha_com_palitos = i
    if NimSum == 0:
        pilhas[pilha_com_palitos] = pilhas[pilha_com_palitos] - 1
        print("A máquina tirou palitos. As pilhas agora são: " + str(pilhas))
    else:
        for i in range(0, len(pilhas)):
            if pilhas[i] ^ NimSum < pilhas[i]:
                pilhas[i] = pilhas[i] ^ NimSum
                print("A máquina tirou palitos. As pilhas agora são: " + str(pilhas))
                break

    return pilhas

if __name__ == "__main__":
    main()