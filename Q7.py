def busca_preco(produto, busca):
    if busca in produto:
        return produto[busca]
    else:
        return "Produto não encontrado"
    
lista_produto = {"Arroz": 10.00, "Café": 38.90, "Macarrão": 5.20}

produto = input("Digite o produto para buscar: ")

preco = busca_preco(lista_produto, produto)

print(f"O preço do(a) {produto} é R${preco: .2f}")