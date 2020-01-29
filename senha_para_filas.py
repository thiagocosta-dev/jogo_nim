# AUTOR: Thiago Costa Pereira

print('=-' * 20)
print('-- GERADOR DE SENHA --'.center(40))
print('=-' * 20)

senhas_comuns = [0]
senhas_pref = [0]

while True:
    print()
    print('--' * 20)
    print('[1] SENHA COMUM')
    print('[2] SENHA PREFERENCIAL')
    print('[3] SAIR')
    print()
    senha = int(input('Escolha sua senha: '))
    print('--' * 20)
    print()

    if senha == 1:

        senhas_comuns.append(int(senhas_comuns[-1]) + 1)
        print(f'Sua senha é: Senha Comum {senhas_comuns[-1]}')

    elif senha == 2:
        senhas_pref.append(int(senhas_pref[-1]) + 1)
        print(f'Sua senha é: Senha Preferencial {senhas_pref[-1]}')

    elif senha == 3:
        print('<<  FINALIZADO  >>')
        break
    else:
        print('ERRO! Digite um valor válido.')
        print()
