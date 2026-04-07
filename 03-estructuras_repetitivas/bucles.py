print("=================== WHILE ===================")
i = 0
while i < 10:
    print("\t[WHILE] iteracion {}".format(i))
    i += 1 ## puede ir al inicio pero en general suele ir al final del bloque

print("=================== FOR ===================")
lista = ['a', 'b', 'c', 'd', 'e']
for i in lista:
    print('[FOR] ', i)

print("=================== RANGE ===================")
for i in range(1, 5):
    print('[RANGE] iteracion {}'.format(i))

print("=================== CONTINUE / BREAK ===================")
for i in range(1, 10):
    if i <= 4:
        continue
    elif i % 7 == 0:
        print('[CONTINUE / BREAK] iteracion {} - ({} % 7 == 0)'.format(i, i))
        break
    else:
        print('[CONTINUE / BREAK] iteracion {}'.format(i))