class user:
    def registration(self):
        full_name = input("Enter your name : ")
        phone_number = int(input("Enter your phone number : "))
        email = input("Enter your email : ")
        address = input("Enter your address : ")
        password = input("Enter your password : ")
        print("Successfully Registered")

    def login(self):
        id = input("Enter your id : ")
        password = input("Enter your password : ")
        print("Successfully logged in")
    
    def new_order(self):
            food = [("Tandoori Chicken", "4 pieces" "INR 240"), ("Vegan Burger",  "1 pieces" "INR 320"),("Truffle Cake",  "500 gms" "INR 900") ]
            order_food = True
            while order_food:    
                print("Please choose a food: ")
                print()
            for food in food:
                print(order_food)
                print()
            while True:
                food = input("which food would you like to order?")
            if food in food:
                print(f"Ordered .")


    def order_history(self):
        pass
    
    def update_profile(self):
        print("*******Update Profile*******")
        food_ID = int(input("Enter food ID : "))
        if food_ID:
            name = input("Enter food name : ")
            quantity = int(input("Enter quantity : "))
            price = input("Enter book price : ")
            discount = input("Enter discount : ")
            stock = float(input("Enter stock : "))

            book.set_name(name)
            book.set_quantity(quantity)
            book.set_price(price)
            book.set_discount(discount)
            book.set_stock(stock)

            print("Successfully Updated")
    

user_obj = user()
user_obj.registration()
user_obj.login()
user_obj.update_profile()