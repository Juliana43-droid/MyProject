# Базовый класс
class Animal:
    def speak(self):
        return "Животное издаёт звук"

# Производный класс
class Dog(Animal):
    def speak(self):
        return "Собака лает"

# Тестовая программа
a = Animal()
d = Dog()

print(a.speak())
print(d.speak())
