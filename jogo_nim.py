'''
AUTOR: THIAGO COSTA PEREIRA
EMAIL: thiago.devpython@gmail.com

Exercício feito para o curso de INTRODUÇÃO À CIÊNCIA DA COMPUTAÇÃO COM PYTHON, oferecido pela USP, através do Coursera.

******************************************************************** INSTRUÇÕES/REGRAS *************************************************

Nesse jogo, n peças são inicialmente dispostas numa mesa ou tabuleiro. Dois jogadores jogam alternadamente,
retirando pelo menos 1 e no máximo m peças cada um. Quem tirar as últimas peças possíveis ganha o jogo.

Existe uma estratégia para ganhar o jogo que é muito simples:
ela consiste em deixar sempre múltiplos de (m+1) peças ao jogador oponente.
******************************************************************* OBJETIVO ***********************************************************

Escrever um programa na linguagem Python, versão 3, que permita a uma "vítima" jogar o NIM contra o computador.
O computador, é claro, deverá seguir a estratégia vencedora descrita acima.

Sejam n o número de peças inicial e m o número máximo de peças que é possível retirar em uma rodada.
Para garantir que o computador ganhe sempre, é preciso considerar os dois cenários possíveis para o início do jogo:

Se n é múltiplo de (m+1), o computador deve ser "generoso" e convidar o jogador a iniciar a partida com a frase "Você começa"
Caso contrário, o computador toma a inciativa de começar o jogo.

Uma vez iniciado o jogo, a estratégia do computador consiste em deixar sempre um número de peças que seja múltiplo de (m+1) ao jogador.
Caso isso não seja possível, deverá tirar o número máximo de peças possíveis.

****************************************************************** CAMPEONATO  ********************************************************

Realiza três partidas seguidas do jogo e, ao final, mostra o placar dessas três partidas e indica o vencedor do campeonato.

'''
 # -*- coding: utf-8 -*-

def computador_escolhe_jogada(n, m):  # Função que devolve um inteiro correspondente à próxima jogada do computador
    computadorRemove = 1              # de acordo com a estratégia vencedora.

    while computadorRemove != m:
        if (n - computadorRemove) % (m + 1) == 0:
            return computadorRemove

        else:
            computadorRemove += 1

    return computadorRemove


def usuario_escolhe_jogada(n, m):  # Solicita que o jogador informe sua jogada e verifica se o valor informado é válido.
                                   # Se o valor informado for válido, a função deve devolvê-lo;
                                   # caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
    jogadaValida = False

    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print('Jogada inválida! POr favor, tente novamente!!.')
            print()

        else:
            jogadaValida = True

    return jogadorRemove


def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('=-=-= Rodada', numeroRodada, '=-=-=')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 PC')


def partida():  # Solicita ao usuário que informe os valores de n e m e
                # inicia o jogo, alternando entre jogadas do computador e do usuário.
    n = int(input('Quantas peças devem ser usadas na partida? '))

    m = int(input('Limite das peças a serem retiradas por jogada? '))

    vezDoPC = False

    if n % (m + 1) == 0:
        print()
        print('Você inicia!')

    else:
        print()
        print('Computador inicia!')
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print('O computador retirou uma peça')
            else:
                print()
                print('O computador retirou', computadorRemove, 'peça(s)')

            vezDoPC = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print('Você retirou uma peça')
            else:
                print()
                print('Você retirou', jogadorRemove, 'peça(s)')
            vezDoPC = True
        if n == 1:
            print('Restam apenas uma peças no tabuleiro.')
            print()
        else:
            if n != 0:
                print('Restam,', n, 'peças no tabuleiro.')
                print()

    print('Fim do jogo! O computador ganhou!')

print('***   Bem-vindo ao jogo do NIM! Escolha:')
print()

print('[1] ==> para jogar uma partida isolada: ')

tipoDePartida = int(input('[2] ==> para jogar um campeonato: '))

if tipoDePartida == 2:
    print()
    print('***Voce escolheu CAMPEONATO!***')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()
