import json

with open("Estoque.json","r") as EstoqueFile:
    estoque = json.loads(EstoqueFile.read())

print("Controle de estoque" "\n 0 - sair" "\n 1 - adicionar item" "\n 2 - remover item" "\n 3 - alterar item" "\n 4 - imprimir estoque")

a = int(input("Faça sua escolha:"))
while a != 0:
    if a == 1:
        b=input('Nome do produto:')
        while b in estoque:
            print('Produto já está cadastrado')
            b=input('Nome do produto:')
        c=int(input('Quantidade inicial:'))
        while c < 0:
            print ('A quantidade inicial não pode ser negativa')
            c=int(input('Quantidade inicial:'))
        estoque[b]=c
        print("O produto {0} foi adicionado na quantidade {1}".format(b,c))
    elif a == 2:
        d = input("Nome do produto:")
        if d in estoque:
            del estoque [d]
            print("Produto removido com sucesso")
        elif d not in estoque:
            print ( " Elemento não encontrado")
    elif a==3:
        f=input("Nome do produto: ")
        if f in estoque:
            g=int(input("Quantidade: "))
            s=-g
            if s>estoque[f] :
                while s>estoque[f]:
                    print(" A quantidade não pode ser negativa")
                    g=int(input("Quantidade: "))
                    s=-g
                if s<=estoque[f]:
                    estoque[f]+=g   
            else:
                estoque[f]+=g
                print ("Novo estoque de {0} é {1} ".format(f,estoque[f]))
        elif f not in estoque:
            print ("Elemento não encontrado")
    elif a == 4:
        print(estoque)
    print("Controle de estoque" "\n 0 - sair" "\n 1 - adicionar item" "\n 2 - remover item" "\n 3 - alterar item" "\n 4 - imprimir estoque")
    a = int(input("Faça sua escolha:"))    
if a == 0:
      print ('Até mais')
      
with open("Estoque.json","w") as EstoqueFile:
    EstoqueFile.write(json.dumps(estoque, sort_keys = True, indent=4))
      
      
