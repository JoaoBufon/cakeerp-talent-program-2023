#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que
#calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#A. salários até R$ 280,00 (incluindo) : aumento de 20%
#B. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#C. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#D. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#E. o salário antes do reajuste;
#F. o percentual de aumento aplicado;
#G. o valor do aumento;
#H. o novo salário, após o aumento.



sal = float(input("Digite o salario:"))

if (sal<=280):
    novo = sal + (sal*0.2)
    perc = "20%"
elif (sal>280 and sal <700):
    novo = sal + (sal*0.15)
    perc = "15%"
elif (sal>=700 and sal<1500):
    novo = sal + (sal*0.1)
    perc = "10%"
else:
    novo = sal + (sal*0.05)
    perc = "5%"

aumento = novo-sal
print("Salario antes do reajuste: ", sal)
print("Percentual de aumento aplicado: ", perc)
print("Valor do aumento: ", aumento)
print("Novo salário: ", novo)