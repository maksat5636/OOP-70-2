# name = data

#def init_test(self, name, lvl, hp):

#pass

#init_test


class Hero:
    #Конструктор класса
    def __init__(self, name, lvl=1, hp=100):
 # атрибуты экземпляра/объекта класса
      self.name = name
      self.lvl = lvl
      self.hp = hp
#метод класса
    def base_action(self):
       return (f"{self.name} this my base action!!")

Kirito = Hero(name="Kirito", lvl=100, hp=1000)
Asuna = Hero(name="Asuna", lvl=100, hp=1000)

Kirito.base_action()
Asuna.base_action()

my_int = int(123)
my_str ="text"