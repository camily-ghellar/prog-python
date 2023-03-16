alunos = []

while True:
    nome_aluno= input("Digite o nome do aluno: ")

    nota1= float(input("Digite a primeira nota: ")) 
    if nota1<0 or nota1>10:
        print ("Digite uma nota válida (0-10)")
        nota1= float(input("Digite a primeira nota: ")) 

    nota2= float(input("Digite a segunda nota: ")) 
    if nota2<0 or nota2>10:
        print ("Digite uma nota válida (0-10)")
        nota2= float(input("Digite a primeira nota: ")) 

    nota3= float(input("Digite a terceira nota: ")) 
    if nota3<0 or nota3>10:
        print ("Digite uma nota válida (0-10)")
        nota3= float(input("Digite a primeira nota: ")) 

    nota4= float(input("Digite a quarta nota: ")) 
    if nota4<0 or nota4>10:
        print ("Digite uma nota válida (0-10)")
        nota4= float(input("Digite a primeira nota: ")) 

    media= (nota1+nota2+nota3+nota4)/4

    situacao = ""

    if media >= 6:
        situacao= "Aprovado"
    else:
        situacao= "Reprovado"

    alunos.append([nome_aluno, media, situacao])



    repetir = str(input("Deseja inserir mais um aluno? [S/N]"))
    if repetir in 'Nn':
        break



print (*alunos)
