preco = float(input('Digite o valor R$'))
desconto = preco * 5 / 100
novo_preco = preco - desconto  
print('Seu preço com desconta vai para R${} reais'.format(novo_preco))