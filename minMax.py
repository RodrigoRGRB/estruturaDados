lista=[5]
n=0

n=int(input('1 numero: '))
lista.append(n)
n=int(input('2 numero: '))
lista.append(n)
n=int(input('3 numero: '))
lista.append(n)
n=int(input('4 numero: '))
lista.append(n)
n=int(input('5 numero: '))
lista.append(n)
min=lista[0]
max=lista[0]

#min
if max<lista[0]:
    max=lista[0]
if max<lista[1]:
    max=lista[1]
if max<lista[2]:
    max=lista[2]
if max<lista[3]:
    max=lista[3]
if max<lista[4]:
    max=lista[4]
#max
if min>lista[1]:
    min=lista[1]
if min>lista[2]:
    min=lista[2]
if min>lista[3]:
    min=lista[3]
if min>lista[4]:
    min=lista[4]
if min>lista[5]:
    min=lista[5]

print('maior %d' %max)
print('menor %d' %min)
