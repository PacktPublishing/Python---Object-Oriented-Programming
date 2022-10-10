class TV:
    def __init__(self):
        self.__status = "off"
        self.__channel = 1
        self.__volume = 50
        
    def __str__(self):
        return f"TV Status:{self.__status} , channel:{self.__channel} , volume:{self.__volume}"
    @property
    def volume(self):
        return self.__volume
    @property
    def channel(self):
        return self.__channel
    @property
    def status(self):
        return self.__status
    
    @volume.setter
    def volume(self, volume):
        # assert volume>=0 and volume<=100, "volume must be between 0 and 100"
        if volume>=0 and volume<=100:
            self.__volume = volume
            
        else:
            raise ValueError("volume must be between 0 and 100")
    
    @channel.setter    
    def channel(self, channel):
        if channel>=1 and channel<=10:
            self.__channel = channel
            
        else:
            raise ValueError("channel must be between 0 and 10")
        
    # volume = property(get_volume , set_volume)
    # channel = property(get_channel , set_channel)
        
tv1 = TV()
# print(tv1.get_volume())
print(tv1.volume)
# print(tv1.get_channel())
print(tv1.channel)
# tv1.set_volume(90)
tv1.volume = 190
# tv1.set_channel(8)
tv1.channel = 18
print(tv1)
