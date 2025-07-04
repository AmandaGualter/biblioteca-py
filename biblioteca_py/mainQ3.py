nome = "Amanda"
sobrenome = "Gualter"

print("Bem vindo a Copiadora", nome, sobrenome, "\n")
total = 0
def escolha_servico():
    while True:
        """seviços disponiveis"""
        print("Entre com o serviço desejado:")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")

        servico = (input(">>>")).lower() #converte para minusculo
        if servico == "dig" or servico == "ico" or servico == "ipb" or servico == "fot":
            return servico
        else:
            print("Serviço inválido. Tente novamente.\n")

#teste de função!!!
servico_escolhido = escolha_servico()
print (f"serviço escolhido: {servico_escolhido}")

if servico_escolhido == "dig":
    print("Valor do serviço por pagina: R$1.10")
elif servico_escolhido == "ico":
    print("Valor do serviço por pagina: R$1.00")
elif servico_escolhido == "ipb":
    print("Valor do serviço por pagina: R$0.40")
elif servico_escolhido == "fot":
    print("Valor do serviço por página: R$0.20")

def num_paginas():
    """Recebe a quantidade de páginas/cópias do usuário."""
    while True:
        try:
            quantidade = int(input("\nEntre com a quantidade de cópias: "))
            if quantidade < 20000:
                return quantidade
            else:
                print("Quantidade inválida. Tente novamente.")
        except ValueError:
            print("Oops! Número de paginas inválido. Tente novamente.")

#teste de função!!!

num_copias = num_paginas()
print(f"Quantidade de cópias: {num_copias}\n")

#VALOR DO SERVIÇO
if servico_escolhido == "dig":
    total = 1.10 * num_copias
elif servico_escolhido == "ico":
    total = 1.00 * num_copias

elif servico_escolhido == "ipb":
    total = 0.40 * num_copias

elif servico_escolhido == "fot":
    total = 0.20 * num_copias

#VALOR DO DESCONTO

if num_copias >= 20 and num_copias < 200:
    desconto = total * 0.15
elif num_copias >= 200 and num_copias < 2000:
    desconto = total * 0.20
elif num_copias >= 2000 and num_copias < 20000:
    desconto = total * 0.25
else:
    desconto = 0

valor_c_desconto = total - desconto

print(f"Valor do serviço: R$ {total:.2f}") #.2f é para usar duas casas decimais
print(f"Valor com desconto: R${valor_c_desconto:.2f}\n")


def servico_extra():
    """Pergunta ao usuário se deseja adicionar mais algum serviço."""
    while True:
        print("Deseja adicionar mais algum serviço?")
        print("1 - Encadernação simples - R$15.00")
        print("2 - Encadernação capa dura - R$40.00")
        print("3 - Não desejo mais nada")
        add = input(">>>")
        if add == "1":
            return add
        elif add == "2":
            return add
        elif add == "3":
            return add
        else:
            print("Entrada inválida. Digite '1', '2' ou '3'.")

#teste de função!!!
extra = servico_extra()

#total = (servico * num_pagina) + extra
if extra == "1":
    valor_total = valor_c_desconto + 15
    print("Valor do servico extra: R$15.00")
    print(f"\nValor total do pedido: R$ {valor_total:.2f}")

elif extra == "2":
    valor_total = valor_c_desconto + 40
    print("Valor do servico extra: R$40.00")
    print(f"\nValor total do pedido: R$ {valor_total:.2f}")

elif extra == "3":
    valor_total = valor_c_desconto + 0
    print(f"\nValor total do pedido: R$ {valor_total:.2f}")


#[EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4]
print("-"*3,"EXTRATO", "-"*3)
print(f"Nome: {nome} {sobrenome}")
print(f"Serviço escolhido: {servico_escolhido}")
print(f"Quantidade de cópias: {num_copias}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor total do pedido: R$ {valor_total:.2f}")
