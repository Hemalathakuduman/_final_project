from admin import admin

class food_operations:
    foodlist = []
    def edit_food(self):
        print("*******Edit Food*******")
        food_ID = int(input("Enter food ID : "))
        if food_ID:
            name = input("Enter food name : ")
            quantity = int(input("Enter quantity : "))
            price = input("Enter book price : ")
            discount = input("Enter discount : ")
            stock = float(input("Enter stock : "))

            food.set_name(name)
            food.set_quantity(quantity)
            food.set_price(price)
            food.set_discount(discount)
            food.set_stock(stock)

            print("Successfully Updated")

            def view_food(self):
                print("*********All Foods*******")
            for food_ID in self.foodlist:
                print(food_ID,"\n")
            
            def remove_food(self):
                print("*******Remove Food******")
    
            food_ID = int(input("Enter food ID : "))
            
            if food_ID:
                self.foodlist.remove(food_ID)
                print("Successfully Deleted")
        