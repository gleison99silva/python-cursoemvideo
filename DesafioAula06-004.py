n = input('Digite algo: ')
print(type(n))
print('Ele é número:', n.isnumeric())
print('Ele é Letra:', n.isalpha())
print('Ele é um Alfanúmero:', n.isalnum())
print('Ele tem Letra Maiúscula:', n.isupper())
print('Ele tem letra minúscula:',n.islower())
print('Ele é um digito:', n.isdigit())