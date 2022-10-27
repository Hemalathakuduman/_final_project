class admin:
    def __int__(self, food_ID,name,quantity,price,discount,stock):
        self.__food_ID = food_ID
        self.__name = name
        self.__quantity = quantity
        self.__price = price
        self.__discount = discount
        self.__stock = stock

    def __str__(self):
        return f"Food ID : {self.__food_ID} \nName : {self.__name} \nQuantity : {self.__quantity} \nPrice : {self.__price} \nDiscount : {self.__discount} \nStock : {self.__stock}"
    
    def set_food_ID(self, food_ID):
        self.__food_ID = food_ID
    
    def get_food_ID(self):
        return self.__food_ID 

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name    

    def set_quantity(self, quantity):
         self.__quantity = quantity
    
    def get_quantity(self, quantity):
         return self.__quantity
         
    def set_price(self, price):
         self.__price =  price
    
    def get_price(self):
         return self.__price

    def set_discount(self, disount):
         self.__discount = disount
    
    def get_discount(self):
         return self.__discount 
    
    def set_stock(self, stock):
         self.__stock = stock
    
    def get_stock(self):
         return self.__stock

if __name__ == "__main__":
    admin_obj = admin(1, "biriyani", "500", 100, 5, 10)
    print(admin_obj)


    

