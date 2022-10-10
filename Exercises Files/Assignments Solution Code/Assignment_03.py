class WeatherCondition:
    def __init__(self,status, temp):
        if status in ["sunny","cloudy","rainy","snowy"]:
            self.__status = status
        else:
            raise ValueError("Status is not valid!")
        
        if temp >=-40 and temp<=40:
            self.__temp = temp
        else:
            raise ValueError("Temp should be between [-40 , 40]")
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self,status):
        if status in ["sunny","cloudy","rainy","snowy"]:
            self.__status = status
        else:
            raise ValueError("Status is not valid!")
        
    @property
    def temp(self):
        return self.__temp
    
    @temp.setter
    def temp(self,temp):
        if temp >=-40 and temp<=40:
            self.__temp = temp
        else:
            raise ValueError("Temp should be between [-40 , 40]")

if __name__ == '__main__':
    weather = WeatherCondition("rainy",20)
    weather.status = "snowy"
    print(weather.status)