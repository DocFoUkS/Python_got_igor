questions = {
    'Как дела?': 'Хорошо',
    'Будешь чай?': 'Нет, я машина. Мне нельзя'
}

while True:
    a = input('Задайте вопрос:')
    if a in questions:
        print(questions[a])
    elif a == 'Пока':
        break
    
    else:
        print('Такого вопроса нет')
            