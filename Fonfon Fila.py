lista1 = []
lista2 = []
lista3 = []


# função para mostrar as filas
def print_filas():
    print ("A lista de pessoas idosas é: ", lista1)
    print ("A lista de pessoas grávidas é: ", lista2)
    print ("A lista de pessoas normais é: ", lista3)
    
# função para inserir na fila (nome, fila)
def insere():
    nome = input("Digite o seu nome: ")
    idoso = input("Você é idoso? ")
    gravi = input("Você está grávida? ")
    gravi = gravi.lower()
    idoso = idoso.lower()
    if idoso=="sim":
        lista1.append(nome)
    elif gravi=="sim":
        lista2.append(nome)
    else:
        lista3.append(nome)

# função que remove da fila e retorne quem foi removido
def remove():
    if len(lista1)> 1: lista1.pop(0)
    if len(lista2)>1: lista2.pop(0)
    if len(lista3)>1: lista3.pop(0)


rodando = True
while rodando:

    print ("1- Sair")
    print ("2-Inserir na fila")
    print ("3-Remover da fila")
    print ("4-Mostrar fila")
    
    opção = int(input("Digite uma opção: "))

    if opção == 1:
        rodando = False
    elif opção == 2:
        insere()
    elif opção == 3:

        removido = remove()
        print ("Próximo", removido)
    elif opção == 4:
        print_filas()
    else:
        print ("Opção inválida")
