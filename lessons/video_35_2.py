#35. Пользовательские метаклассы. Параметр metaclass
# Создание Через отдельный Класс - На практике удобнее этим методом, тк в этом случае в руках вся мощь ООП
# и можно создавать Иерархии Метаклассов.

class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MIN_COORD': 0, 'MAX_COORD': 200})
        return type.__new__(cls, name, base, attrs)
    # То же самое через __init__
    # def __init__(cls, name, base, attrs):
    # super().__init__(name, base, attrs) # на всякий случай
    # cls.MIN_COORD = 0
    # cls.MAX_COORD = 200

class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)

# --- RUN --------------------------------

pt1 = Point()
print(pt1.MAX_COORD)
print(pt1.get_coords())