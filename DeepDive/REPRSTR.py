# class Human:
#     def __str__(self):
#         return "I am Vaihslai"
#
#     def __repr__(self):
#         return "<Vaishali>"
#
# h= Human()
# print(h)
from abc import ABCMeta, abstractmethod
class AbstractClass(metaclass=ABCMeta):
    @abstractmethod
    def eatfood(self):
        pass