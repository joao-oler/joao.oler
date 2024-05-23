n1 = int(input("Digite numero inicial: "))
n2 = int(input("Digite numero final: "))

tamanho = n2 - n1 

if (tamanho > 100):
    print("Invalido")
else:
    for i in range(n1, n2 + 1):
        print(i)

        