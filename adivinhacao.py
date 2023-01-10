import random

bem_vindo = "Bem vindo ao jogo da adivinhacao"

print("\n")
print("*"*40)
print(bem_vindo.center(40))
print("*"*40)

total_tentativas = 0
resposta = 'S'
pontuacao_total = 0
pontos = 0

while(resposta != "N"):
    resposta = " "
    numero_adivinhacao = random.randrange(1,101)
    print(numero_adivinhacao)
    print("• Qual nivel de dificuldade?")
    print("  (1) Facil (2) Medio (3) Dificil")

    nivel = int(input("  → Qual nivel deseja: "))
    validacao = 0
    
    while(validacao != 1):
        if(nivel == 1):
            total_tentativas = 20
            pontos = 25
            validacao = 1
        elif(nivel == 2):
            total_tentativas = 10
            validacao = 1
            pontos = 50
        elif(nivel == 3):
            total_tentativas = 5
            pontos = 100
            validacao = 1
        else:
            print("\nValor incorreto, digite novamente!")
            nivel = int(input("→ Qual nivel deseja: "))

        for rodada in range(5, total_tentativas + 1):
            print(f'\n• Tentativa {rodada} de {total_tentativas}')
            chute = int(input('Digite o numero de chute: '))
            while(total_tentativas!=0):
                if(chute > numero_adivinhacao):
                    print("O seu chute é maior que o numero")
                    total_tentativas = total_tentativas-1
                    break
                elif(chute < numero_adivinhacao):
                    print("O seu chute é menor que o numero")
                    total_tentativas = total_tentativas-1
                    break
                elif(total_tentativas == 0):
                    print(f"\n\nGame Over!\nPontuação final: {pontuacao_total}\n")
                    break
                else:
                    print(f"\n♥ Parabens, você acertou!\n• O numero a ser adivinhado era: {numero_adivinhacao}")
                    pontuacao_total = pontuacao_total + pontos
                    while(resposta != "N" and resposta != "S"):
                        resposta = str(input("→ Você deseja continuar? [S] / [N]: ")).upper()
                        if(resposta == "S"):
                            print(f"Pontuacao atual: {pontuacao_total}")
                            print("-"*40)
                            break
                        elif(resposta == "N"):
                            print(f"\n\nGame Over!\nPontuação final: {pontuacao_total}\n")
                            break
                        else: 
                            print("\nValor incorreto, digite apenas [S] / [N]")
                            resposta = str(input("→ Você deseja continuar? [S] / [N]: ")).upper()
                    break
print("*"*40)
print("*"*40)
