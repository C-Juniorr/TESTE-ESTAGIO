valor = (int(input('Digite um valor: ')))
fibona = [0, 1]  

while fibona[-1] < valor:
    p_valor = fibona[-1] + fibona[-2]
    fibona.append(p_valor)
    print(fibona)

if valor in fibona:
    print('O valor esta na sequencia da fibonacci! {}'.format(valor))
else:
    print("O valor nao esta ná sequencia! ")
