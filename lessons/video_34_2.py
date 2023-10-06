#34. Метаклассы. Объект type
class BBB: pass
class CCC: pass

def method_dict(self):
    print(self.__dict__)


AAA = type('Point', (BBB, CCC), {'MIN_COORD': 0,
                                 'MAX_COORD': 200,
                                 'method_dict_A': method_dict,
                                 'method_1': lambda self: print(self.MAX_COORD)
                                 })
# То же самое обычной записью:
# class Point(BBB, CCC):
#     MIN_COORD = 0
#     MAX_COORD = 200
# AAA = type('Point', (), {'MIN_COORD': 0, 'MAX_COORD': 200}) # если не наследует классы

# Посмотрим Базоввввые классы для данного класса
print(AAA.__mro__)
pt1 = AAA()
pt1.method_dict_A()
pt1.method_1()

