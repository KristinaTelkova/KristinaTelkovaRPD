d = {
    'стул': 'chair',
    'стол': 'table',
    'яблоко': 'apple',
}
while True:
    rus = input('Введите слово на русском для перевода(или "q" для выхода): ').strip().lower()
    if rus == 'q':
        print('Приятно было пообщаться!')
        break
    if rus in d:
        print(f'Слово {rus} переводится как "{d[rus]}"')
    else:
        print(f'К сожалению, я не знаю слово "{rus}"')
        new_word = input(f'А как слово "{rus}" переводится:')
        d[rus] = new_word
        print(f'Теперь я знаю перевод слова "{rus}". Это - "{d[rus]}"')