# AULA - 09/04 #

# EXERCÍCIO 1#
'''contagem_multiplos_3 = 0
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 3 == 0:
        contagem_multiplos_3 += 1
print(f"Quantidade de números múltiplos de 3: {contagem_multiplos_3}")'''

# EXERCÍCIO 2 #
'''senhacorreta = 'heloisalinda123'
while True:
    senha = input("Digite a senha:")
    if senha == senhacorreta:
        print("SENHA CORRETA! SEJA BEM VINDA!")
        break
    else:
        print("SENHA INCORRETA!TENTE NOVAMENTE!")'''

# EXERCÍCIO 3 #
'''print("MENU DA HELO")
print("---------------------------------------")
menu=int(input("Digite para escolher uma das opções:\n"
               "[0]-Entrar\n"
               "[1]-Sair\n"))
while menu !=2:
    if menu == 0:
        print("Você entrou! Seja bem vinda fofa :)")
    elif menu == 1:
        print("Bye bye, você saiu! Até logo :(")
        break
    else:
        print("Não existe essa opção escolha outra!")
    print("\nDigite para escolher uma das opções:")
    menu = int(input("[0]-Entrar\n"
                     "[1]-Sair\n"))'''

# EXERCÍCIO 5#
'''senhacorreta = 'heloisalinda123'
contador = 3
while contador >0:
    senha=input("Digite a senha:")
    contador = contador - 1
    if senha == senhacorreta:
        print("SENHA CORRETA! SEJA BEM VINDA!")
        break
    else:
        print("SENHA INCORRETA!")
    if contador == 0:
        print("Acesso negado!")'''

# EXERCÍCIO 8 #
'''import random
opcoes = ['cara','coroa']
contador = 0
while contador <3:
    lancamento = random.choice(opcoes)
    print(lancamento)
    contador = contador+1'''