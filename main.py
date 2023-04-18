print("Digite o número que quer testa")
N = int(input("> "))
i = 1
while True:
    i = i + 1
    if N ==1:
        print("Não primo")
        break
    if N <=0:
        print("Número inválido")
        break
    if N % i ==0 and i !=N:
        print("Não primo")
        break
    if N % i ==0 and i ==N:
        print("Primo")
        break
