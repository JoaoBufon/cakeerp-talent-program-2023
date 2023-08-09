#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu
# respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem
#lida.

idades=[]
alturas=[]
x=1

while x <=5:
    idade = int(input("Digite sua idade: "))
    idades.append(idade)
    altura = float(input("Digite sua altura em m: "))
    alturas.append(altura)
    x = x+1
    
x=4
while x >= 0:
    print(idades[x])
    print(alturas[x])
    x = x-1