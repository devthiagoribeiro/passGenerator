from random import sample

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = lower_case.upper()
numbers = '1234567890'
symbols = '!@#$%&'

size = int(input('Digite o tamanho da senha que deseja gerar(8-12): '))

forpass = lower_case + upper_case + numbers + symbols
password = ''.join(sample(forpass, size))

print(password)