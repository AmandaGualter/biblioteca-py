# Informcoes do cliente
nome = "Amanda"
sobrenome = "Gualter"

# Mensagem de boas vindas
print("Bem vindo a loja", nome, sobrenome)

# Caixas de entrada
valor_unitario = float(input("Informe o valor do produto: "))
quantidade = int(input("Informe a quantidade do produto: "))

valor = valor_unitario * quantidade

print("Valor sem desconto:" , valor)

# Se valor for menor que 2500 o desconto será de 0%; 
if valor < 2500:
    desconto = valor * 0.00
    print("Valor com desconto: R$", (valor - desconto) )

# Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%; 
elif valor >= 2500 and valor < 6000:
    desconto = valor * 0.04
    print("Valor com desconto: R$", (valor - desconto) )

# Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%;
elif valor >= 6000 and valor < 10000:
    desconto = valor * 0.07
    print("Valor com desconto: R$", (valor - desconto) )

# Se valor for igual ou maior que 10000 o desconto será de 11%;
else:
    desconto = valor * 0.11
    print("Valor com desconto: R$", (valor - desconto) )
