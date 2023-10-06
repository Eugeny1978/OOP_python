#35. Пользовательские метаклассы. Параметр metaclass
# Создание Через Функцию (в учебных целях)

# class Point:
#     MIN_COODR = 0
#     MAX_COODR = 200

def create_class_point(name, base, attrs):
    attrs.update({'MIN_COODR': 0, "MAX_COORD": 200})
    return type(name, base, attrs)

class Point(metaclass=create_class_point):
    def get_coords(self):
        return (0, 0)

# --- RUN --------------------------------

pt1 = Point()
print(pt1.MAX_COORD)
print(pt1.get_coords())