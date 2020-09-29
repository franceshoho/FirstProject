"""
Module of making different restaurant menus
    - make sandwich
    - make pizza
    - make drinks
"""

def make_sandwich(customer, order, *ingredients, quantity=1):
    # *ingredients - tuple of ingredients will be passed in
    # quantity is default arg, and needs to come after
    # also, you need to specify keyword to make it clear to python
    print(f'for customer:  {customer}')
    print(f'{quantity} of {order} sandwich(es) with following ingredients:')
    for ingredient in ingredients:
        print(f'- {ingredient}')

def make_pizza(customer, *toppings, quantity=1, size='large'):
    # make a pizza of a size with toppings specified by customer
    # requires only customer and at toppings as var
    print(f'for customer:  {customer}')
    print(f'{quantity} of size {size} with following toppings:')
    for topping in toppings :
        print(f'- {topping}')

def make_drink(customer, kind, quantity=1, size='large'):
    # make a pizza of a size with toppings specified by customer
    # requires only customer and at toppings as var
    print(f'for customer:  {customer}')
    type = kind.lower()
    simple_drinks = ['beer', 'tea', 'coffee', 'soft drink', 'wine']
    ingredients = ['mint', 'vodka', 'soda', 'syrup']
    if type not in simple_drinks:
        print(f'{quantity} {type} drink needs the following toppings:')
        for ingredient in ingredients :
            print(f'- {ingredient}')
    else:
        print(f'\t{quantity} {type} drink is on the way')