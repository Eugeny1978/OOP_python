#36. Метаклассы в API ORM Djangoю Пример использования Метаклассов

class Meta(type):
    def __init__(cls, name, bases, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

class Women1(metaclass=Meta):
    title = 'Header'
    content = 'any content'
    photo = 'path to photo'


# МетаКласс Meta превращает класс Women1 в Women2:

class Women2:
    title = 'Header'
    content = 'any content'
    photo = 'path to photo'
    class_attrs = {'title': 'Header', 'content': 'any content', 'photo': 'path to photo'}
    def __init__(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

class Women3:
    title = 'Header'
    content = 'any content'
    photo = 'path to photo'

# --- RUN ---------------------------------------

w1 = Women1()
w2 = Women2()
w3 = Women3()
print(w1.__dict__, '\n')
print(w2.__dict__, '\n')
print(w3.__dict__)
print(w3.title, w3.content, w3.photo, sep=' | ')