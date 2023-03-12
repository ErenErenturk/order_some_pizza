import csv
import datetime


# Create a class object for components of pizza (both the pizza name and the topping)
class Component(object):
    def __init__(self, name, description, price):
        self.name = name
        self.price = price
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


# Create an upper_class object named 'Decorator'
class Decorator(Component):
    def get_cost(pizza, topping):
        return Component.get_cost(pizza) + Component.get_cost(topping)

    def get_description(pizza, topping):
        return Component.get_description(pizza) + ' ' + Component.get_description(topping)

# Control id number to get either it is valid or not
def isvalid_id(value):
    value = str(value)
    if not len(value) == 11:
        return False
    if not value.isdigit():
        return False
    if int(value[0]) == 0:
        return False
    digits = [int(d) for d in str(value)]
    if not sum(digits[:10]) % 10 == digits[10]:
        return False
    if not (((7 * sum(digits[:9][-1::-2])) - sum(digits[:9][-2::-2])) % 10) == digits[9]:
        return False
    return True

# Control card number to get either it is valid or not
def isvalid_card(card):
    card = str(card)
    if not len(card) == 16:
        return False
    if not card.isdigit():
        return False
    if int(card[0]) == 0:
        return False
    return True


# Define some pizza classes
pizza1 = Component('Margherita', 'Fresh mozzarella, basil, and tomato sauce', 8.99)
pizza2 = Component('Pepperoni', 'Pepperoni and mozzarella cheese', 9.99)
pizza3 = Component('Meat Lover', 'Pepperoni, sausage, ham, and bacon', 12.99)
pizza4 = Component('Veggie', 'Mushrooms, onions, green peppers, and black olives', 10.99)
pizza5 = Component('Supreme', 'Pepperoni, sausage, onions, green peppers, and mushrooms', 13.99)

# Define some topping classes
topping1 = Component('Olive', 'with extra olive', 1.24)
topping2 = Component('Mushroom', 'with extra mushroom', 1.99)
topping3 = Component('Cheese', 'with extra cheese', 1.49)
topping4 = Component('Meat', 'with extra meat', 2.49)
topping5 = Component('Garlic', 'with extra garlic', 1.74)
topping6 = Component('Corn', 'with extra corn', 0.99)


# Define a main function to get an order from customer
def main():
    # open the menu file
    with open('menu.txt', 'r') as menu:
        print(menu.read())
        menu.close()

    # Pizza choice
    pizza_list = [pizza1, pizza2, pizza3, pizza4, pizza5]
    while True:
        pizza_id = input('Enter the id of your pizza: ')

        try:
            pizza_id = int(pizza_id) - 1  # pizza_id = 1 - 1
            if pizza_id in range(len(pizza_list)):
                break
            else:
                print(f'Please, enter a number between [{1, len(pizza_list)}]')
        except:  # if input is not totally integer
            print('Please, enter an integer!')

    pizza = pizza_list[pizza_id]
    print(f'Your selected pizza: {pizza.get_name()}\nIngredients: {pizza.get_description()}\n')

    # Topping choice
    topping_list = [topping1, topping2, topping3, topping4, topping5, topping6]

    while True:
        topping_id = input('Enter the id of your topping: ')

        try:
            topping_id = int(topping_id) - 11  # topping_id = 11 - 11
            if topping_id in range(len(topping_list)):
                break
            else:
                print(f'Please, enter a number between [{11, len(topping_list) + 10}]')
        except ValueError:  # if input is not totally integer
            print('Please, enter an integer!')
        # topping_id = 11 - 11

    topping = topping_list[topping_id]
    print(f'Your selected topping: {topping.get_name()}\n')

    total_cost = Decorator.get_cost(pizza, topping)
    pizza_name = pizza.get_name()
    pizza_desc = Decorator.get_description(pizza, topping).lower()
    topp_name = topping.get_name()
    print(f'Your order is Pizza {pizza_name}; it has {pizza_desc}\nAnd it costs only {total_cost}$')

    # Create variables to save personal data about the customer
    fullname = input('\nYour name and surname: ')
    tc_id = input('Your ID number: ')
    while not isvalid_id(tc_id):
        print('Invalid input!')
        tc_id = input('Please enter a valid card number: ')
    card_num = input('Credit card number: ')
    while not isvalid_card(card_num):
        print('Invalid input!')
        card_num = input('Please enter a valid card number: ')
    password = input('Password: ')

    # List that we want to add as a new row
    new_order_info = [
        fullname, tc_id, card_num, password, total_cost, pizza_name, pizza_desc, topp_name, datetime.datetime.now()
    ]

    # Save info to csv file
    with open('Orders_Database.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_order_info)


main()
