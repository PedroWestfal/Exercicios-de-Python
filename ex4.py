n = input('Digite algo aqui:')
print('O tipo primitivo deste valor é', type(n))
print('Só tem espaços?', n.isspace())
print('É um numero?', n.isnumeric())
print('É alfabetico?', n.isalpha())
print('Esta em maiusculas?', n.isupper())
print('Esta em minusculas?', n.islower())
print('Esta capitalizada?', n.istitle())