""" summry line
fooditem(name, price)
Burger(fooditem)
Pizza(fooditem)
Drink(fooditem)
"""
from abc import ABC, abstractmethod

class RestaurentOwner:
    order_list = []

    def add_order(self, order):
        self.order_list.append(order)

class Customer:
    def __init__(self, name):
        self.name = name

owner = RestaurentOwner()



class Fooditem(ABC):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    @abstractmethod
    def prepare(self):
        pass


class Burger(Fooditem):
    def __init__(self):
        super().__init__('Burger', 150)
    
    def prepare(self):
        print('Grilling the burger patty and adding sauce...')
    
    def __repr__(self):
        return self.get_name()

class Pizza(Fooditem):
    def __init__(self):
        super().__init__('Pizza', 300)
    
    def prepare(self):
        print('Baking the pizza with cheese and topping...')

    def __repr__(self):
        return self.get_name()
    
class Drink(Fooditem):
    def __init__(self):
        super().__init__('Drink', 50)
    
    def prepare(self):
        print('Pouring the drink into the cup...')

    def __repr__(self):
        return self.get_name()

class Order:
    def __init__(self):
        self.items = []
        owner.add_order(self)
    
    def add_item(self, food_item):
        self.items.append(food_item)
    
    def process_order(self):
        print('\tPreparing your items:')
        for item in self.items:
            item.prepare()

    def show_order(self):
        print('\n\tYour Order Summary')
        total = 0
        for item in self.items:
            print(f'- {item} - {item.get_price()}') # Polymorphism
            total += item.get_price()
        print(f'Total price: {total} BDT.')

    def __repr__(self):
        items_name = ''
        for item in self.items:
            items_name += f'{item.get_name()}, '
        return f'[{items_name}]'


while True:
    burger = Burger()
    pizza = Pizza()
    drink = Drink()

   
    

    print('Choose an Option')
    print('1. Owner')
    print('2. Customer')
    print('3. Exit')

    option = int(input('Enter Your Option: '))

    if option == 1:
        '''Owner'''
        # order = Order()
        '''Order list iterate process order, show order : HomeWork'''
        while True:
            print("Select an Option\n"
               "1. Process Order\n"
               "2. Show Order\n"
               "3. Exit")
            owner_selection = int(input('Enter Your Option: '))
            if owner_selection == 1:
                for i in range(len(owner.order_list)):
                    print(f'\n Order {i+1}: ')
                    owner.order_list[i].process_order()

            elif owner_selection == 2:
                for i in range(len(owner.order_list)):
                    print(f'\n Order {i+1}: ')
                    owner.order_list[i].show_order()
            elif owner_selection == 3:
                break
            else:
                print('Wrong input. Try Again')

    elif option == 2:
        '''Customer'''
        name = input('Enter your name: ')
        customer = Customer(name)
        order = Order()
        item_list = [burger, pizza, drink]

        while True:
            print("Select an Option\n"
              "1. Show Menu\n" 
              "2. Add Item\n" 
              "3. Exit")
            customer_selection = int(input('Enter Your Option: '))
            if customer_selection == 1:
                for i in range(len(item_list)):
                    print(f'{i} {item_list[i]}')

            elif customer_selection == 2:
                order_input = int(input('Enter item code: '))
                order.add_item(item_list[order_input])
            
            elif customer_selection == 3:
                break
            else:
                print('Wrong input. Try Again')


    elif option == 3:
        break
    else:
        print('Wrong input. Try Again')
