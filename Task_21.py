# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Выходные данные:'лповап ываываыв'
import os
os.system('cls')


def sort_text(text):
    li = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(li)


text = 'ываабв лповап абвцукв алоабвабв ываываыв'
new_text = sort_text(text)
print(f'На вход подается следующий текст: \n{text}')
print(f'Текст без слов, содержащих "абв", следующий: \n{new_text}')

