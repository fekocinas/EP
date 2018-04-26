from firebase import firebase

firebase = firebase.FirebaseApplication("https://tentativa2-bfe74.firebaseio.com/",None)

if firebase.get("pasta",None) is None:
    estoque = {}
else:
    estoque = firebase.get("pasta",None)
print("Programa de estoque de lojas" "\n 0 - Encerrar programa" "\n 1 - Acessar loja"  "\n 2 - Adicionar loja" "\n 3 - Excluir loja" "\n 4 - Imprimir lojas")
resp = int(input("Faça sua escolha:"))  


while resp != 0:

    while resp == 1:
        
        nome_loja = input("Digite o nome da loja:")
        
        if nome_loja not in estoque:
            
            print("Loja não encontrada")
            
        elif nome_loja in estoque:

            print("Controle de estoque" "\n 0 - sair" "\n 1 - adicionar item" "\n 2 - remover item" "\n 3 - alterar quantidade do item" "\n 4 - imprimir estoque" "\n 5 - alterar preço do item" "\n 6 - Saldo do estoque")
            a = int(input("Faça sua escolha:"))
            
            while a != 0 :
                
                
                if a == 1:
                    
                    b=input('Nome do produto:')
                    
                    while b in estoque[nome_loja]:
                        
                        print('Produto já está cadastrado')
                        b=input('Digite o nome de outro produto:')
                        
                    c=int(input('Quantidade inicial:'))
                    estoque[nome_loja][b]={"Quantidade":c}
                    g=float(input("Preço: ")) 
                    
                    while g<0:
                        
                        print ('O preço não pode ser negativo')
                        g=float(input('Digite o preço novamente:'))
                        
                    estoque[nome_loja][b]["Preço"]=g    
                    print("Item cadastrado")
                    
                    
                elif a == 2:
                    
                    d = input("Nome do produto:")
                    
                    if d in estoque[nome_loja]:
                        del estoque[nome_loja][d]
                        firebase.delete("pasta/{0}".format(nome_loja),d)
                        print("Produto excluído")
                        a = 0
                        
                    elif d not in estoque[nome_loja]:
                        print ( " Elemento não encontrado")
                        
                        
                elif a==3:
                    
                    f=input("Nome do produto: ")
                    
                    if f in estoque[nome_loja]:
                        g=int(input("Quantidade: "))
                        estoque[nome_loja][f]["Quantidade"]+=g   
                        print("Quantidade alterada")
                   
                        
                    elif f not in estoque[nome_loja]:
                        print ("Elemento não encontrado")
                    
                       
                        
                elif a == 4:
                    
                    print(estoque[nome_loja])
                    
                    
                elif a==5:
                    
                    h=input("Nome do produto: ") 
                    
                    if h not in estoque[nome_loja]:
                        print ("Produto não encontrado")
                        
                    else:    
                        i=float(input("Preço: "))
                        estoque[nome_loja][h]["Preço"]=i
                        print("Preço alterado")
                        
                    
                elif a==6:
                    
                    k = 0
                    
                    for produto in estoque[nome_loja]:
                        k += estoque[nome_loja][produto]["Quantidade"]*estoque[nome_loja][produto]["Preço"]
                    print("O saldo da {0} é de {1}" .format(nome_loja,k))
                
                print("Controle de estoque" "\n 0 - sair" "\n 1 - adicionar item" "\n 2 - remover item" "\n 3 - alterar quantidade do item" "\n 4 - imprimir estoque" "\n 5 - alterar preço do item" "\n 6 - Saldo do estoque")
                a = int(input("Faça sua escolha:"))
                    

            if a == 0:       
                  print ("Saída da loja efetuada")
                  resp = 0
     

                           
    
    if resp == 2:
        
        nome_loja = input("Digite o nome da nova loja:")
        
        if nome_loja in estoque:
            
            print("Loja já cadastrada")

            
        else:
            estoque[nome_loja] = {}
            print("{0} adicionada com sucesso" .format(nome_loja))

            


    elif resp == 3:
        
        nome_loja = input("Digite o nome da loja que vai ser excluída:")
        
        if nome_loja not in estoque:
            print("Loja não encontrada")
            
        elif nome_loja in estoque:
            del estoque[nome_loja]
            firebase.delete("pasta",nome_loja)
            print("{0} excluída com sucesso".format(nome_loja))

        
        
    elif resp == 4:
        for i in estoque:
            print(i)
            
    print("Programa de estoque de lojas" "\n 0 - Encerrar programa" "\n 1 - Acessar loja"  "\n 2 - Adicionar loja" "\n 3 - Excluir loja" "\n 4 - Imprimir lojas")
    resp = int(input("Faça sua escolha:"))  
            
    

        
        
firebase.patch("/pasta",estoque)
print("Programa encerrado")
