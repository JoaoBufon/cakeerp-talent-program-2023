#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor=[]
x=1

while x <=5:
    leitor = int(input("Digite um numero inteiro: "))
    vetor.append(leitor)
    x = x+1

print(vetor)