# Димическая генерация классов

# Класс от которого будут наследоваться метаклассы
class Base:
    def __str__(self):
        return 'my_class'


# кортеж с классами для наследования
bases = (
    Base,
)


# методы доступные в классе, созданном на основе метакласса
def get_first_name(self):
    return self.first_name


def get_last_name(self):
    return self.last_name


def init(self, first_name, last_name):
    self.last_name = last_name
    self.first_name = first_name


attrs = {
    'first_name': '',
    'last_name': '',
    'get_first_name': get_first_name,
    'get_last_name': get_last_name,
    '__init__': init,
}

# 1 Использование type
# type - класс! не функция
#   type(<имя класса>,
#        <кортеж родительских классов>, # для наследования, может быть пустым
#        <словарь, содержащий атрибуты и их значения>)

User = type('User', bases, attrs)
user_type = User('Vasya', '123')
print(user_type.get_first_name())


# 1 Использование metaclass=
class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100

class X(metaclass=Meta):
    pass

print(X.attr)
