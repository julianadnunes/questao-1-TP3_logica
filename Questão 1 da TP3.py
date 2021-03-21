valor_consumo = float(input('Informe o valor total do consumo no restaurante?: '))
pessoas = int(input('Informe a quantidade de pessoas que consumiram no restaurante?: '))
taxa = float(input('Informe o percentual do serviço do restaurante?: ' ))

    
if pessoas < 0 or taxa <= 0 or taxa > 100:
    print('Valor Inváido!')
    
else:
    valor_total = float(((valor_consumo * taxa)/100)+ valor_consumo)
    valor_total = str(valor_total)
    valor_total.replace('.',',')
    
    print('O valor total da conta com o percentual de serviço é R$ {valor_total} reais')
    
  #  valor_divido = float(valor_total/pessoas)
  #  print(f'O valor total da conta divido entre as pessoa(s) é R$ {valor_divido:.2f} reais')
    
        #print(f'O valor total da conta com o percentual de serviço é R$ {valor_total:.2f}reais')
    #calculo_valor_total = float()
    #print(str(f'{n:.2f}%')) 
#        elif:
        #print('Valor inválido')
    
print('Fim do programa"')
    
"""print(str('valor do percentual é (n/100)  ')

    

'''if genero == 'masculino' or genero == 'm':
    n1 = float(72.7 * h) - 58
    print('Você é do gênero Masculino')
    print(f' Seu peso ideal é {n1:.2f}KG')
    
if genero == 'feminino' or genero == 'f':
    n2 = float(62.1 * h) - 44.7
    print('Você é do gênero Feninino')
    print(f' Seu peso ideal é {n2:.2f}KG')
    
print("Fim do programa!")"""