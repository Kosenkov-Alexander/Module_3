# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(text):
    '''
    Функция принимает строку, а возвращает слова с заглавной первой буквой
    :param text: string, принимает текст
    :return: string, возвращает текст с заглавной первой буквой
    '''
    return (text.title())
print(int_func('first second third'))