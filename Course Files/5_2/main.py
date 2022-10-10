class ShoppingList():
    def __init__(self):
        self.items = [ "apple", "banana" , "milk", "carrot"]
        
    def __getitem__(self,idx):
        return self.items[idx]

        
shoppinglist = ShoppingList()

print(shoppinglist[0])
# print(shoppinglist.items[0])
print("======================")
for item in shoppinglist:
    print(item)
print("======================")
if "milk" in shoppinglist:
    print("you have to buy milk")
    
