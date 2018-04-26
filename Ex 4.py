import json

with open("Estoque.json","r") as EstoqueFile:
    estoque = json.loads(EstoqueFile.read())

    
    
    print("Controle de estoque" "\n 0 - sair" "\n 1 - adicionar item" "\n 2 - remover item" "\n 3 - alterar quantidade do item" "\n 4 - imprimir estoque" "\n 5 - alterar preço do produto" "\n 6 - Saldo do estoque")
    
    
    a = int(input("Faça sua escolha: "))
        
    while a != 0:
        if a == 1:
            b=input('Nome do produto:')
            while b in estoque:
                print('Produto já está cadastrado')
                b=input('Nome do produto:')
            c=int(input('Quantidade inicial:'))
            estoque[b]={"Quantidade":c}
            g=float(input("Preço: ")) 
            while g<=0:
                print ('O preço não pode ser negativo')
                g=float(input('Preço:'))
            estoque[b]["Preço"]=g    
            
        elif a == 2:
            d = input("Nome do produto:")
            if d in estoque:
                del estoque[d]
            elif d not in estoque:
                print ( " Elemento não encontrado")
        elif a==3:
            f=input("Nome do produto: ")
            if f in estoque:
                g=int(input("Quantidade: "))
                estoque[f]["Quantidade"]+=g   
            elif f not in estoque:
                print ("Elemento não encontrado")
        elif a == 4:
            print(estoque)
        elif a==5:
            h=input("Nome do produto: ")
            while h not in estoque:
                print ("Produto não encontrado")
                h=input("Digite novamente o nome do produto: ")
            i=float(input("Preço: "))
            while i <= 0:
                i = float(input("O preço não pode ser negativo,digite outro valor:"))
            estoque[h]["Preço"]=i
        elif a==6:
            k = 0
            for produto in estoque:
                k += estoque[produto]["Quantidade"]*estoque[produto]["Preço"]
            print("O saldo de {0} é {1}" .format(produto,k))
        print("Controle de estoque" "\n 0 - sair" "\n 1 - adicionar item" "\n 2 - remover item" "\n 3 - alterar quantidade do item" "\n 4 - imprimir estoque" "\n 5 - alterar preço do produto" "\n 6 - Saldo do estoque")
        a = int(input("Faça sua escolha:"))   
            
    if a == 0:
          print ('Até mais')

    with open("Estoque.json","w") as EstoqueFile:
        EstoqueFile.write(json.dumps(estoque, sort_keys = True, indent=4))
