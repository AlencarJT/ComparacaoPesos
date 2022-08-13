l = []
p = []
ma = me = 0
while True:
    p.append(str(input('Digite o nome: ')))
    p.append(float(input('Digite o peso: ')))
    if len(l) == 0:
        ma = me = p[1]
    else:
        if p[1] > ma:
            ma = p[1]
        if p[1] < me:
            me = p[1]
    l.append(p[:])
    p.clear()
    while True:
        r = str(input('Deseja Continuar? ')).strip().lower()
        if r in 'SsnN':
            break
    if r in 'Nn':
        break
print('*'*60)
print(f'Foram cadastradas {len(l)} pessoas')
print(f'O maior peso foi de {ma:.2f} kg, de ', end='')
for h in l:
    if h[1] == ma:
        print(f'[{h[0]}]', end=' ')
print()
print(f'O menor peso foi de {me:.2f} kg, de ', end='')
for h in l:
    if h[1] == me:
        print(f'[{h[0]}]', end=' ')