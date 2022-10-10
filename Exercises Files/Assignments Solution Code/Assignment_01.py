class Player:
    MAX_HEARTS = 3
    def __init__(self,name):
        self.name = name
        self.hearts = Player.MAX_HEARTS
        
    def __str__(self):
        return f"Player {self.name} , {self.hearts}"
    
    def lose(self):
        if self.hearts>1:
            self.hearts-=1
            print(f"You Lost, But you have {self.hearts} more hearts")
        else:
            print("Game Over!")
if __name__ == '__main__':
    player = Player("John")
    print(player)
    player.lose()
    player.lose()
    player.lose()
