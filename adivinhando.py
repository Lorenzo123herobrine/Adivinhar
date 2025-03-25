import random

print ("----------------------------------------------")
print ("Bem vindo ao jogo favorito do piurepay")

numero_secreto = round (random.randrange(1,31))
total_de_tentativas = 10
pontos = 1000

print("Qual o nivel de dificuldade que você aguenta?\n")
print("(1)Easy (2)Normal (3)Hard")

nivel = int(input("Digite o nivel desejado:"))

if (nivel == 1):
    total_de_tentativas = 20      
    
elif (nivel == 2):
    total_de_tentativas = 10
    
else:
    total_de_tentativas = 5

for rodada in range (1,total_de_tentativas): 
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute = int (input ("Digite o numero secreto de 1 a 30: "))
    print ("---------------------------------------------------------")
    print (f"Você digitou {chute}")

    if (numero_secreto == chute):
        print(f"Acertou sortudo! Sua pontos foi {pontos} pontos!")
        break

    else:
        if(chute > numero_secreto): 
            print("Pensou muito alto, o número secreto é menor.")
            print("---------------------------------------------------")
        
        if(chute < numero_secreto):  
            print ("Chutou baixo? O número secreto é maior.")
            print("---------------------------------------------------")
        
        if (chute >= 1000):
            print("Pode ter certeza que é menor que mil.")
            print("---------------------------------------------------")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos



