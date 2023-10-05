from typing import Callable, Type, TypeVar, Union


Tip = Callable[[Union["A", "B"]], Union[int, str]]
class A:
    @staticmethod
    def foo():
        pass

class B:
    pass


def create(cls: A) -> str:
   return "A"

def createB(cls: B) -> int:
   return 1

def krom(f : Tip):
    pass

krom(createB)