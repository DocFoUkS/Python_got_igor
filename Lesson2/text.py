import codecs

dict_colvo_bukv_a = {
    'А': 0,
    'а': 0
}


def countA(line):
    dict_colvo_bukv_a['А'] +=line.count('А')
    dict_colvo_bukv_a['а'] +=line.count('а')


def reverse(stroka):
    mass_line = stroka.replace('\n', '').split(' ')
    reverseline = ''
    for revel in range(-1,  -1*len(mass_line), -1):
        reverseline +=mass_line[revel] + ' '
    print(reverseline)



with codecs.open(r'Lesson2\war.txt', 'r', encoding='UTF-8') as fileopen:
    for line in fileopen:
        reverse(line)
        countA(line)
print(dict_colvo_bukv_a)