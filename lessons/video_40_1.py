# S - Single Responsibility Principle (Принцип Единственной Ответственности)

import os

class Computer:

    def __init__(self, name, memory_size):
        self.name: str = name
        self.memory_size: int = memory_size

# В больших Проектах предпочтительно эти методы (см ниже) вынести в отдельных Класс,
# тк со временем могут меняться методы способы сохраниения и загрузки
# (например в облако или другие форматы файлов)
# Оставив в классе только определениие локальных переменных.
    # Закоментирую:
    # def save(self):
    #     print(f'Сохранение объекта {self} в файл')
    # def load(self):
    #     print(f'Загрузка данных объекта {self} из файла')

# Исправить можно создав Отдельный Класс:
class SaveComputer:
    def save_to_file(self, path_to_file, data: str):
        ishas_info = bool(os.path.getsize(path_to_file))
        try:
            with open(path_to_file, 'a') as file:
                if ishas_info:
                    data_format = '\n' + data
                else:
                    data_format = data
                file.write(data_format)
        except Exception as error:
            print(error)

# --- RUN -----------------------------------

c1 = Computer('Intel', 32)
c2 = SaveComputer()
print(c1.__dict__)
c2.save_to_file('test_file_video_40_1.txt', str(c1.__dict__))
