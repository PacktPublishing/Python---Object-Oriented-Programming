class ShoppingList:
    def __init__(self,items):
        self.items = items
        
    @classmethod
    def from_string(cls , text):
        items = text.split(',')
        return cls(items)
    

if __name__ == "__main__":
    l1= ShoppingList(["Banana","milk"])
    l2= ShoppingList.from_string("Banana,Milk")

    print(l1.items)
    print(l2.items)
        