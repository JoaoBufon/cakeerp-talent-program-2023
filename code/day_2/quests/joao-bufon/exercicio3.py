perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
cont=0

for pergunta in perguntas:
    resposta = input(pergunta+" s ou n: ")
    if (resposta == 's'):
        cont = cont+1
    
if (cont==2):
    print("Suspeita")
elif (cont>2 and cont<5):
    print("Cúmplice")
elif (cont==5):
    print("Assasino")
else:
    print("Inocente")
    