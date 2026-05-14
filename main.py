vendas = 0
valor_total = 0
total_descontos = 0
total_liquido = 0




print("=== SISTEMA DE VENDAS ===")
print("1 - Registrar venda")
print("2 - Ver resumo parcial")
print("3 - Encerrar sistema")

while True:
    
    escolha = int(input("Digite sua escolha: "))

    if escolha == 1:
        vendas = vendas + 1
        print("=== REGISTRAR VENDA ===")
        nome_produto = input("Digite o nome do produto: ")
        valor_uni = float(input("Digite o valor da venda: "))
        valor_total = valor_total + valor_uni
        quantidade = int(input("Digite a quantidade: "))
        print("=== VENDA REGISTRADA ===")

    if escolha == 2:

        print("=== RESUMO PARCIAL ===")
        print("Nome do produto: ", nome_produto)
        print("Valor unitário: R$", valor_uni)
        print("Quantidade: ", quantidade)
        valor_bruto = valor_uni * quantidade
        print("Valor Bruto: R$", valor_bruto)

        if valor_bruto >= 1000:
            desconto = valor_bruto * 0.15
            valor_final = valor_bruto - desconto
            valor_total = valor_total + valor_final
            total_descontos = total_descontos + desconto
            total_liquido = total_liquido + valor_final
            print("=== DESCONTO DE 15% ===")
            print("Valor com desconto: R$", valor_final)
            print("Desconto de 15%")
            print("Valor economizado: R$", desconto)
            print("Total de vendas: ", vendas)
            print("Valor total: R$", valor_total)
            print("Total de descontos: R$", total_descontos)
            print("Total liquido: R$", total_liquido)


        elif valor_bruto >= 500 and valor_bruto <= 999.99:   
            desconto = valor_bruto * 0.10
            valor_final = valor_bruto - desconto
            valor_total = valor_total + valor_final
            total_descontos = total_descontos + desconto
            total_liquido = total_liquido + valor_final
            print("=== DESCONTO DE 10% ===")
            print("Valor com desconto: R$", valor_final)
            print("Desconto de 10%")
            print("Valor economizado: R$", desconto)
            print("Total de vendas: ", vendas)
            print("Valor total: R$", valor_total)
            print("Total de descontos: R$", total_descontos)
            print("Total liquido: R$", total_liquido)


        elif valor_bruto >= 100 and valor_bruto <= 499.99:   
            desconto = valor_bruto * 0.5
            valor_final = valor_bruto - desconto
            valor_total = valor_total + valor_final
            total_descontos = total_descontos + desconto
            total_liquido = total_liquido + valor_final
            print("=== DESCONTO DE 5% ===")
            print("Valor com desconto: R$", valor_final)  
            print("Desconto de 5%")
            print("Valor economizado: R$", desconto) 
            print("Total de vendas: ", vendas)
            print("Valor total: R$", valor_total)
            print("Total de descontos: R$", total_descontos)
            print("Total liquido: R$", total_liquido)

        else:
            print("Sem desconto")
            valor_final = valor_bruto
            desconto = 0
            print("Total de vendas: ", vendas)
            
            

    elif escolha == 3:
        break

 

