from __future__ import annotations
from enum import Enum


class Positions(Enum):
    JUNIOR = 10  
    MIDDLE = 15
    SENIOR = 20  
  
  
class Programmer:
    def __init__(self, name: str, position: Positions, time: int = 0) -> None:
        self.__name = name
        self.__position = position
        self.__time = time
        self.__hour_price = self.__position

    def work(self, time: int) -> None:
        self.__time += time

    def rise(self) -> None:
        if self.__position == Positions.JUNIOR.value:
            self.__position = Positions.MIDDLE.value
            self.__hour_price = Positions.MIDDLE.value

        elif self.__position == Positions.MIDDLE.value:
            self.__position = Positions.SENIOR.value
            self.__hour_price = Positions.SENIOR.value

        else:
            self.__hour_price += 1

    def info(self) -> str:
        return f'{self.__name}: {self.__time} ч. {self.__give_salary()} тгр.'

    def __give_salary(self) -> int:
        salary = self.__hour_price * self.__time
        self.__time = 0
        return salary


if __name__ == '__main__':
    programmer_0 = Programmer('Ivan', Positions.JUNIOR.value)
    programmer_0.work(10)
    print(programmer_0.info())

    programmer_0.rise()
    programmer_0.work(10)
    print(programmer_0.info())

    programmer_0.rise()
    programmer_0.work(10)
    print(programmer_0.info())

    programmer_0.rise()
    programmer_0.work(10)
    print(programmer_0.info())

