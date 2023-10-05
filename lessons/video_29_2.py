# 29. Обработка исключений. Блоки finally и else

# Открытие Файла лучше делать используя конструкци with / она автоматически закрывает файл после использования


path_to_file_1 = 'test_file_video_29.txt'
path_to_file_2 = 'test_file_video_29_Error.txt'
mode1 = 'r'
mode2 = 'w'
def open_file(path_to_file, mode):
    try:
        with open(path_to_file, mode) as file:
            file.write('Add any information')
    except Exception as error:
        print(error)

# Пытаюсь записать в файл информацию
open_file(path_to_file_1, mode1) # Ошибка: Файл открыт ТОЛЬКО для чтения
# Ошибка: Неверный Путь к Файлу или файл отсутствует. Однако конструкция создает такой файл и ошибка устраняется.
open_file(path_to_file_2, mode2)

