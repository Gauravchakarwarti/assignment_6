class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock


class Admin:
    def __init__(self):
        self.food_items = []
        self.food_id_counter = 1

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = self.food_id_counter
        food = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food)
        self.food_id_counter += 1
        print("Food item added successfully.")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food in self.food_items:
            if food.food_id == food_id:
                food.name = name
                food.quantity = quantity
                food.price = price
                food.discount = discount
                food.stock = stock
                print("Food item edited successfully.")
                return
        print("Food item not found.")

    def remove_food_item(self, food_id):
        for food in self.food_items:
            if food.food_id == food_id:
                self.food_items.remove(food)
                print("Food item removed successfully.")
                return
        print("Food item not found.")

    def view_food_items(self):
        for food in self.food_items:
            print(f"Food ID: {food.food_id}")
            print(f"Name: {food.name}")
            print(f"Quantity: {food.quantity}")
            print(f"Price: {food.price}")
            print(f"Discount: {food.discount}")
            print(f"Stock: {food.stock}")
            print("---------------------")

    


class User:
    def __init__(self, full_name, mobile_number, email, address, password):
        self.full_name = full_name
        self.mobile_number = mobile_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_order(self, selected_items):
        ordered_items = []
        for item_index in selected_items:
            if item_index <= len(admin.food_items):
                food = admin.food_items[item_index - 1]
                ordered_items.append(food)
        self.order_history.append(ordered_items)
        print("Order placed successfully.")

    def view_order_history(self):
        for order in self.order_history:
            print("Ordered Items:")
            for food in order:
                print(f"Food ID: {food.food_id}")
                print(f"Name: {food.name}")
                print(f"Quantity: {food.quantity}")
                print(f"Price: {food.price}")
                print(f"Discount: {food.discount}")
                print("---------------------")
            print("=====================")

    def update_profile(self, full_name, mobile_number, email, address, password):
        self.full_name = full_name
        self.mobile_number = mobile_number
        self.email = email
        self.address = address
        self.password = password
        print("Profile updated successfully.")



admin = Admin()


admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
admin.add_food_item("Vegan Burger", "1 piece", 320, 0, 5)
admin.add_food_item("Truffle Cake", "500gm", 900, 0, 2)


admin.view_food_items()


user = User("Gaurav chakarwarti", "9839140180", "gauravc@gmail.com", "123 Street, gkp", "password")


user.place_order([2, 3])


user.view_order_history()
user.update_profile("vivan", "9798654410", "vivan1211@gmail.com", "432 Road near dm bunglow gkp", "newpassword")



