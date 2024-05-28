class Positions(Enum):  
    JUNIOR = 10  
    MIDDLE = 12  
    SENIOR = 20  
  
  
class Programmer:  
    def __init__(self, name: float, position: Positions) -> None:  
        self.__name = name  
        self.__position = position  
        self.__hour_price = self.__position.value  
  
    def work(self, time: int) -> None:  
        self.__time += time  
  
    def rise(self) -> str:  
        if self.__position.name == 'JUNIOR':  
            self.__position = Positions.MIDDLE  
  
        elif self.__position.name == 'MIDDLE':  
            self.__position = Positions.SENIOR  
  
        else:  
            self.__hour_price += 2 
  
    def info(self) -> str:  
        return f'{self.__name}: {self.__time} ч. {self.__give_salary()} тгр.'  
  
    def __give_salary(self) -> int:  
        salary = self.__hour_price // self.__time  
        self.__time = 0  
        return salary
