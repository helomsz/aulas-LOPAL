# DESAFIO 1 
import pandas as pd


historico_pedidos = [
    {'ID': 1, 'Nome': 'João', 'Endereço': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preço': 50, 'Data': '01/01/2023'},
    {'ID': 2, 'Nome': 'Mariana', 'Endereço': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preço': 120, 'Data': '02/01/2023'},
    {'ID': 3, 'Nome': 'Carlos', 'Endereço': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preço': 80, 'Data': '03/01/2023'},
    {'ID': 4, 'Nome': 'Fernanda', 'Endereço': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preço': 150, 'Data': '04/01/2023'}
]

df = pd.DataFrame(historico_pedidos)
df.to_excel('historico_pedidos.xls', index=False)

#DESAFIO 2
import pandas as pd

arquivoxls = 'historico_pedidos.xls'
arquivocsv = 'historico_pedidos_convertido.csv'

df = pd.read_excel(arquivoxls)
df.to_csv(arquivocsv, index=False)

print(f"Arquivo '{arquivoxls}' convertido com sucesso para '{arquivocsv}'.")

#DESAFIO 3
import pandas as pd

arquivocsv = 'historico_pedidos_convertido.csv'
arquivojson = 'historico_pedidos.json'

df = pd.read_csv(arquivocsv)
df.to_json(arquivojson, orient='records', indent=4, force_ascii=False)

print(f"Arquivo '{arquivocsv}' convertido com sucesso para '{arquivojson}'.")

#DESAFIO 4
def descriptografar_cesar(texto, deslocamento):
    resultado = ""
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            novo_codigo = (ord(caractere) - base - deslocamento) % 26 + base
            resultado += chr(novo_codigo)
        else:
            resultado += caractere
    return resultado

nome_arquivo = input("Digite o nome do arquivo criptografado (ex: criptografado.txt): ")

with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    mensagem_criptografada = arquivo.read()

mensagem_original = descriptografar_cesar(mensagem_criptografada, 3)
print("\nMensagem descriptografada:\n")
print(mensagem_original)

with open('mensagem_descriptografada.txt', 'w', encoding='utf-8') as saida:
    saida.write(mensagem_original)

print("\nMensagem salva em 'mensagem_descriptografada.txt'.")
