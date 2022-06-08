# Напишите программу, удаляющую из текста все слова содержащие "абв", 
# которое регистронезависимо. Используйте знания с последней лекции. 
# Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

line = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
words = line.split(' ')
def del_word(words):
    fragment = 'абв'
    new_words = []
    for i in words:
        if fragment not in i:
            new_words.append(i)
    return new_words
del_word(words)
print(del_word(words))


