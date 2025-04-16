# AULA - 09/04 #

# EXERCÍCIO 1#
'''numeros = 1
contador = 0
for numeros in range (1,11):
    numero = int(input("Digite o número desejado: "))
    if numero %3==0:
        contador = contador + 1
print(f"Quantidade de números múltiplos de 3: {contador}")'''

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

#EXERCÍCIO 4 #
'''valor_inicial = int(input("Digite o valor inicial, inteiro:"))
valor_final = int(input("Digite o valor final, inteiro:"))

if valor_inicial > valor_final:
    print("Inválido! O valor inicial precisa ser menor!")
num = int(input("Digite um número: "))

if num >= 2:
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} não é primo")
            break
    else:
        print(f"{num} é primo")
else:
    print(f"{num} não é primo")'''

        
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

'''# EXERCÍCIO 6 #
pares = []
impares = []
for i in range(1, 11):  
    numero = int(input("Digite o número desejado: "))
    if numero % 2 == 0:
        pares.append(numero)  
    else:
        impares.append(numero) 
print("\nNúmeros pares digitados:", pares)
print("Números ímpares digitados:", impares)'''

# EXERCÍCIO 7 #
'''frase = input("Digite uma frase: ").lower()  
contagem_a = 0
contagem_e = 0
contagem_i = 0
contagem_o = 0
contagem_u = 0
for letra in frase:
    if letra == 'a':
        contagem_a += 1
    elif letra == 'e':
        contagem_e += 1
    elif letra == 'i':
        contagem_i += 1
    elif letra == 'o':
        contagem_o += 1
    elif letra == 'u':
        contagem_u += 1
print(f"Quantidade de 'a': {contagem_a}")
print(f"Quantidade de 'e': {contagem_e}")
print(f"Quantidade de 'i': {contagem_i}")
print(f"Quantidade de 'o': {contagem_o}")
print(f"Quantidade de 'u': {contagem_u}")'''

# EXERCÍCIO 8 #
'''import random
opcoes = ['cara','coroa']
contador = 0
while contador <3:
    lancamento = random.choice(opcoes)
    print(lancamento)
    contador = contador+1'''

'''# EXERCÍCIO 9 #
numeros = []
quantidade = int(input("Quantos números você vai digitar? "))
for i in range(quantidade):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)
media = sum(numeros) / len(numeros)
menores_que_media = sum(1 for numero in numeros if numero < media)
print(f"A média dos números é: {media}")
print(f"Quantos números são menores que a média: {menores_que_media}")'''

'''# EXERCÍCIO 10 #
numeros = []
valores = int(input("Digite quantos números você deseja verificar:"))
for i in range(valores):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)
if len(numeros) < 2:
    print("É necessário ter pelo menos dois números para encontrar o segundo maior.")
else:
    maior = segundo_maior = numeros[0]
    for numero in numeros[1:]:  
        if numero > maior:
            segundo_maior = maior
            maior = numero
        elif numero > segundo_maior and numero != maior:
            segundo_maior = numero
    print(f"O segundo maior número da sequência é: {segundo_maior}")'''

# DESAFIOS
#coelhos
'''populacao = float(input("Digite o número inicial de coelhos: "))
taxa_reproducao = float(input("Digite a taxa de reprodução (ex: 0.3 para 30%): "))
taxa_mortalidade = float(input("Digite a taxa de mortalidade (ex: 0.1 para 10%): "))
geracoes = int(input("Digite o número de gerações: "))

for i in range(1, geracoes + 1):
    nascimentos = populacao * taxa_reproducao
    mortes = populacao * taxa_mortalidade
    populacao = populacao + nascimentos - mortes

    print(f"Geração {i}: {int(populacao)} coelhos")

print(f"\nPopulação final após {geracoes} gerações: {int(populacao)} coelhos")'''

#forca
'''import random

palavras = ["Márcia", "computador", "python", "programa", "caligrafia", "desespero", "incerteza"]
palavra_secreta = random.choice(palavras)

letras_certas = []
letras_erradas = []
tentativas = 6

while True:
    exibicao = ""
    for letra in palavra_secreta:
        if letra in letras_certas:
            exibicao += letra + " "
        else:
            exibicao += "_ "

    print("\nPalavra:", exibicao.strip())
    print(f"Letras erradas: {' '.join(letras_erradas)}")
    print(f"Tentativas restantes: {tentativas}")

    if all(letra in letras_certas for letra in palavra_secreta):
        print("\n Parabéns! Você acertou a palavra:", palavra_secreta)
        break

    if tentativas == 0:
        print("\n Você perdeu! A palavra era:", palavra_secreta)
        break

    tentativa = input("Digite uma letra: ").lower()

    if tentativa in letras_certas or tentativa in letras_erradas:
        print("Você já tentou essa letra e eu já disse que não tem. Tente outra.")
        continue

    if tentativa in palavra_secreta:
        letras_certas.append(tentativa)
        print("Boa! A letra está na palavra.")
    else:
        letras_erradas.append(tentativa)
        tentativas -= 1
        print("Essa letra não está na palavra fofo(a).")'''
