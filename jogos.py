print("--------------------------------------")
print("----------- jogo do advinha-----------")
print("--------------------------------------")

numero_secreto = 42
total_tentivas = 3
rodada = 1

while(rodada <= total_tentivas):
    print("tentivas:", rodada, "de", total_tentivas)
    chute = input("digite o numero: ")

    print("você digitou", chute)

    chuteConvertido = int(chute)
    soma = 32 + chuteConvertido

    if(numero_secreto == chuteConvertido):
        print("voce acertou e soma dos valores é ", soma)
    else:
        if(chuteConvertido > numero_secreto):
            print("voce errou, o seu chute foi maior que o numero secreto")
        elif(chuteConvertido < numero_secreto):
            print("voce errou, o seu chute foi menor do que o numero secreto")

        rodada = rodada + 1