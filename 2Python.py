primeiro_num= float(input("Digite o primeiro número: ") )
segundo_num= float(input("Digite o segundo número: "))
terceiro_num= float(input("Digite o terceiro número: "))
quarto_num= float(input("Digite o quarto número: "))
quinto_num= float(input("Digite o quinto número: "))



maior_num= primeiro_num
if maior_num<segundo_num:
    maior_num= segundo_num

if maior_num<terceiro_num:
    maior_num=terceiro_num

if maior_num<quarto_num:
    maior_num=quarto_num

if maior_num<quinto_num:
    maior_num=quinto_num

print ("O maior dos números informados é o", maior_num)



menor_num= primeiro_num
if menor_num>segundo_num:
    menor_num= segundo_num

if menor_num>terceiro_num:
    menor_num=terceiro_num

if menor_num>quarto_num:
    menor_num=quarto_num

if menor_num>quinto_num:
    menor_num=quinto_num

print ("O menor dos números informados é o", menor_num)