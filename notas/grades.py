n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
media = ((n1*2)+n2+(n3*2))/5

if media >= 6 :
    print("Aluno aprovado! ")
else :
    if media >= 3 :
        print("Em exame! ")
    else: 
        print("Aluno reprovado: ")
