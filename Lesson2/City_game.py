import codecs

mass_towns = []
with codecs.open(r'Lesson2\towns.txt', 'r', encoding='UTF-8') as fileopen:
    for line in fileopen:
        mass_towns.append(line.replace('\n', '').upper())


def town_game(city):
    global mass_towns
    if city in mass_towns:
        mass_towns.remove(city)
        last = city.replace('Ь', '').replace('Ы', '').replace('Ъ', '').replace('Ё', '')[-1].upper()
        mark = 0
        for town in mass_towns:
            first = town[0]
            if last == first:
                print(town.capitalize())
                mass_towns.remove(town)
                mark = 1
                break
        if mark == 0:
            print ('Ты выиграл!')
    else:
        print('Такого города нет в списке')       


while True:
    city = input('Введите город: ').upper()
    if city.capitalize() != 'Пока':
        town_game(city)
    else:
        break
