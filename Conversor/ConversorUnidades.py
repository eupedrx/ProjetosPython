def centimetros(x):
    return x * 100


def milimetros(x):
    return x * 1000


def milhas(x):
    return x * 1609


def conversor():
    print("Selecione o tipo de Unidade para converter")
    print("1 - Centimetros")
    print("2 - Milimetros")
    print("3 - Milhas")

    escolha = input("Digite o número da unidade escolhida:")

    if escolha in ['1', '2', '3']:
        num1 = float(input("Digite em Metros o quanto você quer converter:"))
        if escolha == '1':
            print(f"{num1} em {escolha} é {centimetros(num1)}")
            if escolha == '2':
                print(f"{num1} em {escolha} é {milimetros(num1)}")
                if escolha == '1':
                    print(f"{num1} em {escolha} é {milhas(num1)}")
                else:
                    print("Escolha inválida.")


conversor()