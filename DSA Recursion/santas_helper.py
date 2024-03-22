class Wish():
    def __init__(self, item_name, price, child_name):
        self.item_name = item_name
        self.price = price
        self.child_name = child_name
        
    def __str__(self) -> str:
        return "{"+f"{self.item_name};{self.child_name};{self.price:.2f}"+"}"
    
    
class SantaHelper():
    def __init__(self) -> None:
        self.wishes = {}
        
        
    def addwish(self, wish:Wish):
        if wish.child_name in self.wishes:
            self.wishes[wish.child_name].append(wish)
        else:
            self.wishes[wish.child_name] = [wish]
            
    def delete(self, child_name):
        return len(self.wishes.pop(child_name))
    
def find(wish):
    return wish.item_name


n = int(input())
santa_helper = SantaHelper()
output = []

for _ in range(n):
    command, params = input().split(" ", 1)
    
    if command == "AddWish":
        item_name, price, child_name = params.split(";")
        wish = Wish(item_name, float(price), child_name)
        santa_helper.addwish(wish)
        output.append("Wish added")
    
    if command == "DeleteWishes":
        child_name = params
        if child_name in santa_helper.wishes.keys():
            deleted_wishes = santa_helper.delete(child_name)
            output.append(f"{deleted_wishes} Wishes deleted")
        else:
            output.append("No Wishes found")
    
    if command == "FindWishesByPriceRange":
        from_price, to_price  = params.split(";")
        
        wish_list = []
        
        for value in santa_helper.wishes.values():
            for wish in value:
                if wish.price >= float(from_price) and wish.price <= float(to_price):
                        wish_list.append(wish)
            wish_list.sort(key=find)
            
        for wish in wish_list:
            output.append(str(wish))
            
        if len(wish_list) == 0:
            output.append("No Wishes found")
            
    if command == "FindWishesByChild":
        child_name = params
        
        wish_list = []
        
        if child_name in santa_helper.wishes.keys():
            for wish in santa_helper.wishes.get(child_name):
                wish_list.append(wish)
            wish_list.sort(key=find)
            for wish in wish_list:
                output.append(str(wish))
        else:
            output.append("No Wishes found")
            
print("\n".join(output))
        
            

            
            
                          
                    
            
        
        
            
    