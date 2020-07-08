a = 1
b = 3
c = a + b

print (c)

d = 'Привет!'
e = 'Как дела?'
f = d + ' ' + e

print (f)

print (d + ' ' + str(a))
print ('Кудык! {} {}'.format(d, a))
print ('Бултых! {d} {a}'.format(d=d, a=a))


g = 5<0
print (g)

x = int(input('Введите число: '))
if x>1 and x<5:
    print ('Игорь молодец!')
else:
    print ('Женя молодец!')

print ('Что-то новое')  