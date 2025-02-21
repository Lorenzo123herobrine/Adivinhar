print ("**************************************")
print ("Bem vindo ao jogo favorito do piurepay")

numero_secreto = 14

print ("***********************")
chute = int (input ("Digite o numero secreto: "))

print (f"Você digitou {chute}")

if (numero_secreto == chute):
    print ("ACERTO FELA DA POLTA")

else:
    if(chute > numero_secreto): 
        print("Errou, seu chute foi maior do que o numero secreto.")

    if(chute < numero_secreto): 
        print ("Chutou baixo? O numero secreto é maior.")
