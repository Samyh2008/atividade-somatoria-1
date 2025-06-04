#calcula o Imc

nome= input('Qual é seu nome? ')
altura= float(input('Qual é sua altura? '))
peso= float(input('Qual é seu peso? '))

imc= peso / (altura ** 2)
print(f'IMC: {imc:.2f}')


if imc <18.5:
    print('Abaixo do peso')
    print('Recomendação: Comer besteira')

elif imc < 24.9:
    print('Peso normal')
    print('Parabéns pela boa forma')

elif imc <29.9:
    print('Sobrepeso')  
    print('Vc ta quase lá')  

elif imc <30.9:
    print('Obesidade Grau I')
    print('Cuidadooo')

elif imc <39.9:
    print('Obesidade Grau II')
    print('Cuidado pra não cair e sair rolando')

else:
    print('Obesidade Grau III (mórbida)') 
    print('Meu deuss jesus')   

