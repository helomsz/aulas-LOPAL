# EXERCÍCIO 1
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

def calcular_imc():
    imc = peso / (altura ** 2)
    return imc

resultado = calcular_imc()
print(f"Você pesa {peso}kg e mede {altura:.2f}m, seu IMC é igual a {resultado:.2f}")

# EXERCÍCIO 2
