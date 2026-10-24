largura = float(input('Digite a largura da parede: '))
pe_direito = float(input('Digite a altura do pé direito: '))
area = largura * pe_direito
cobertura = area / 2
print('Você tem {:.0f}m² de parede.'.format(area))
print('Sabendo que cada litro de tinta pinta uma área de 2m²\nVocê vai precisar de {:.0f} latas de tinta para pintar os {:.0f}m² de parede.'.format(cobertura, area))