#include <stdio.h>

void jogar(int pilhas[], int npilhas);
void movimento_da_pessoa(int pilhas[], int npilhas);
int escolhe_pilha(int pilhas[], int npilhas);
int escolhe_palitos(int pilhas[], int pilha_escolhida);
void movimento_da_maquina(int pilhas[], int npilhas);

int main() {
    int pilhas[100];
    int npilhas;

    printf("Quantas pilhas são? ");
    scanf("%d", &npilhas);

    for (int i = 0; i < npilhas; i++) {
        printf("Quantos palitos tem a pilha %d? ", i + 1);
        scanf("%d", &pilhas[i]);
    }

    jogar(pilhas, npilhas);

    return 0;
}

void jogar(int pilhas[], int npilhas) {
    int primeiro;

    printf("Quem começa? (Digite 1 para o jogador ou 0 para a máquina) ");
    scanf("%d", &primeiro);

    if (primeiro == 1) {
        movimento_da_pessoa(pilhas, npilhas);
    }

    while (1) {
        int soma = 0;
        for (int i = 0; i < npilhas; i++) {
            soma += pilhas[i];
        }

        if (soma == 0) {
            printf("A máquina ganhou!\n");
            break;
        }

        movimento_da_maquina(pilhas, npilhas);

        soma = 0;
        for (int i = 0; i < npilhas; i++) {
            soma += pilhas[i];
        }

        if (soma == 0) {
            printf("Você ganhou!\n");
            break;
        }

        movimento_da_pessoa(pilhas, npilhas);
    }
}

void movimento_da_pessoa(int pilhas[], int npilhas) {
    int pilhas_com_palitos[100];
    int npilhas_com_palitos = 0;

    for (int i = 0; i < npilhas; i++) {
        if (pilhas[i] > 0) {
            pilhas_com_palitos[npilhas_com_palitos] = i + 1;
            npilhas_com_palitos++;
        }
    }

    int pilha_escolhida = escolhe_pilha(pilhas_com_palitos, npilhas_com_palitos);
    int npalitos = escolhe_palitos(pilhas, pilha_escolhida);

    pilhas[pilha_escolhida - 1] -= npalitos;

    printf("Você tirou palitos. As pilhas agora são: ");
    for (int i = 0; i < npilhas; i++) {
        printf("%d ", pilhas[i]);
    }
    printf("\n");
}

int escolhe_pilha(int pilhas_com_palitos[], int npilhas_com_palitos) {
    int pilha;

    while (1) {
        printf("De qual pilha você quer tirar palitos? Escolha entre ");
        for (int i = 0; i < npilhas_com_palitos; i++) {
            printf("%d ", pilhas_com_palitos[i]);
        }
        printf(": ");
        scanf("%d", &pilha);

        int pilha_valida = 0;
        for (int i = 0; i < npilhas_com_palitos; i++) {
            if (pilha == pilhas_com_palitos[i]) {
                pilha_valida = 1;
                break;
            }
        }

        if (pilha_valida) {
            return pilha;
        } else {
            printf("Essa pilha não tem palitos\n");
        }
    }
}

int escolhe_palitos(int pilhas[], int pilha_escolhida) {
    int palitos;

    while (1) {
        printf("Quantos palitos você quer tirar? ");
        scanf("%d", &palitos);

        if (palitos > pilhas[pilha_escolhida - 1]) {
            printf("Essa pilha não tem tantos palitos\n");
        } else if (palitos < 1) {
            printf("Você deve tirar pelo menos um palito\n");
        } else {
            return palitos;
        }
    }
}

void movimento_da_maquina(int pilhas[], int npilhas) {
    int NimSum = 0;
    int pilha_com_palitos = 0;

    for (int i = 0; i < npilhas; i++) {
        NimSum ^= pilhas[i];
        if (pilhas[i] > 0) {
            pilha_com_palitos = i + 1;
        }
    }

    if (NimSum == 0) {
        pilhas[pilha_com_palitos - 1]--;
        printf("A máquina tirou palitos. As pilhas agora são: ");
        for (int i = 0; i < npilhas; i++) {
            printf("%d ", pilhas[i]);
        }
        printf("\n");
    } else {
        for (int i = 0; i < npilhas; i++) {
            if ((pilhas[i] ^ NimSum) < pilhas[i]) {
                pilhas[i] -= NimSum;
                printf("A máquina tirou palitos. As pilhas agora são: ");
                for (int j = 0; j < npilhas; j++) {
                    printf("%d ", pilhas[j]);
                }
                printf("\n");
                break;
            }
        }
    }
}