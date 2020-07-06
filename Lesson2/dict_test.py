dict_test = {
    1: 'yes', 
    0: 'no'
    }

mass_test = [1, 2, 3, 4]

print (mass_test[0])

print (dict_test[1])

if mass_test[1] in dict_test:
    print (dict_test[mass_test[1]])
else:
    print ('Такого ключа нет')

print (dict_test.get(mass_test[1], {2: 'not'}))

print (dict_test)

mass_test.append('0')

dict_test['3'] = 'xor'

print (mass_test)
print (dict_test)

mass_test.append(5)
dict_test[10] = 'Привет'
print (mass_test)
print (dict_test)
