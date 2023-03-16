alunos= []

#aluno 1
nome_aluno1= input("Digite o nome do primeiro aluno: ")
nota1_aluno1= float(input("Digite a primeira nota do primeiro aluno: "))    
nota2_aluno1= float(input("Digite a segunda nota do primeiro aluno: "))    
nota3_aluno1= float(input("Digite a terceira nota do primeiro aluno: "))    
nota4_aluno1= float(input("Digite a quarta nota do primeiro aluno: "))    

media_aluno1= (nota1_aluno1+nota2_aluno1+nota3_aluno1+nota4_aluno1)/4

alunos.append([nome_aluno1, media_aluno1])


#aluno 2
nome_aluno2= input("Digite o nome do segundo aluno: ")
nota1_aluno2= float(input("Digite a primeira nota do segundo aluno: "))    
nota2_aluno2= float(input("Digite a segunda nota do segundo aluno: "))    
nota3_aluno2= float(input("Digite a terceira nota do segundo aluno: "))    
nota4_aluno2= float(input("Digite a quarta nota do segundo aluno: "))    

media_aluno2= (nota1_aluno2+nota2_aluno2+nota3_aluno2+nota4_aluno2)/4

alunos.append([nome_aluno2, media_aluno2])


#aluno 3
nome_aluno3= input("Digite o nome do terceiro aluno: ")
nota1_aluno3= float(input("Digite a primeira nota do terceiro aluno: "))    
nota2_aluno3= float(input("Digite a segunda nota do terceiro aluno: "))    
nota3_aluno3= float(input("Digite a terceira nota do terceiro aluno: "))    
nota4_aluno3= float(input("Digite a quarta nota do terceiro aluno: "))    

media_aluno3= (nota1_aluno3+nota2_aluno3+nota3_aluno3+nota4_aluno3)/4

alunos.append([nome_aluno3, media_aluno3])


#sem quebra de linha
print(*alunos)

#com quebra de linha
print(nome_aluno1, "- média geral:", media_aluno1) 
print(nome_aluno2, "- média geral:", media_aluno2) 
print(nome_aluno3, "- média geral:", media_aluno3)


#aluno com a maior média
maior_media= media_aluno1
if maior_media<media_aluno2:
    maior_media= media_aluno2
if maior_media<media_aluno3:
    maior_media=media_aluno3



if maior_media==media_aluno1:
    print ("O aluno que obteve a maior média foi", nome_aluno1)

elif maior_media==media_aluno2:
    print ("O aluno que obteve a maior média foi", nome_aluno2)

elif maior_media==media_aluno3:
    print ("O aluno que obteve a maior média foi", nome_aluno3)



#aluno com a menor média
menor_media= media_aluno1
if menor_media>media_aluno2:
    menor_media= media_aluno2
if menor_media>media_aluno3:
    menor_media=media_aluno3



if menor_media==media_aluno1:
    print ("O aluno que obteve a menor média foi", nome_aluno1)

elif menor_media==media_aluno2:
    print ("O aluno que obteve a menor média foi", nome_aluno2)

elif menor_media==media_aluno3:
    print ("O aluno que obteve a menor média foi", nome_aluno3)

