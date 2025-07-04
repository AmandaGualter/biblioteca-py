nome = "Amanda"
sobrenome = "Gualter"

print("Bem vindo a loja de gelados", nome, sobrenome)
print("------------CARDÁPIO-----------")
print("Tamanho  |  Cupuaçu  |  Açaí   ")
print("   P     |  RS 9.00  | RS 11.00")
print("   M     |  RS 14.00 | RS 16.00")
print("   G     |  RS 18.00 | RS 20.00")

total = 0

while True:
    #VERIFICAÇÃO DE SABOR E TAMANHO
    sabor = input("Qual sabor gostaria de comprar(CP/AC)?")
    if sabor != "cp" and sabor != "ac":
        print("Sabor invalido. Tente novamente.")
        continue

    tamanho = input("Qual tamanho gostaria de comprar(P/M/G)?")
    if tamanho != "p" and tamanho != "m" and tamanho != "g":
        print("Tamanho invalido. Tente novamente.")
        continue
    
    if sabor == "ac" and tamanho == "p":
        total = total + 11.00
    elif sabor == "ac" and tamanho == "m":
        total = total + 16.00
    elif sabor == "ac" and tamanho == "g":
        total = total + 20.00
    elif sabor == "cp" and tamanho == "p":
        total = total + 9.00
    elif sabor == "cp" and tamanho == "m":
        total = total + 14.00
    elif sabor == "cp" and tamanho == "g":
        total = total + 18.00
    else:
        print("Invalido")
    
    #ADICIONAR ITEM A LISTA DE COMPRA
    add = input("Algo mais(S/N)?:")
    if add == "n":
        break
    elif add == "s":
        continue


print(f"o total é {total}")