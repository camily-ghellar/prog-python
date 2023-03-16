primeiro_num= float(input("Digite o primeiro número: ") )
segundo_num= float(input("Digite o segundo número: "))
terceiro_num= float(input("Digite o terceiro número: "))
quarto_num= float(input("Digite o quarto número: "))
quinto_num= float(input("Digite o quinto número: "))

lista_num = [primeiro_num, segundo_num, terceiro_num, quarto_num, quinto_num]

num_pares = []
for n in lista_num:
    if n % 2 == 0:
        num_pares.append(n)

print("Dos números informados,", num_pares, "é/são número(s) par(es)")


num_impares = []
for n in lista_num:
    if n % 2 != 0:
        num_impares.append(n)

print("Dos números informados,", num_impares, "é/são número(s) ímpar(es)")

print ("A média geral dos números informados é", (primeiro_num + segundo_num + terceiro_num + quarto_num + quinto_num)/5 )
