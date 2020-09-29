"""
Passing Arguments into Function
When ordering arguments within a function or function call, arguments
need to occur in a particular order:

    Formal positional arguments
    *args
    Keyword arguments
    **kwargs
"""
import restaurant as r

def describe_city(city, country="USA"):
    print(f'{city} is located in {country}.')

def get_formatted_name(first, last, middle=""):
    # return formatted name
    # if there's a middle name
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()

def build_person(person, first, last, middle="", age=None):
    """return a dictionary of persons"""
    if last not in person:
        person[last] = {}
    person[last]['first'] = first
    if middle:
        person[last]['middle'] = middle
    if age:
        person[last]['age'] = age

def build_profile(first, last, middle="", **user_info):
    # will put everything we know about user in user_info dict
    # **kwargs are passed into dict user_info already
    # so we just need to add first, last, middle (if any)
    user_info['first'] = first
    user_info['last'] = last
    if middle:
        user_info['middle'] = middle
    return user_info

def graph_circle(radius, color="black", **kwargs):
    # graph a circle using radius, with default color line black
    # use kwargs to unpack other options user passes in
    print(f"We are graphing a {color} circle of radius = {radius}")
    print(f"other requirements are:")
    for key, value in kwargs.items():
        print(f'\t{key} = {value}')

def sum_integers(*nums):
    # return sum of integers, but we can pass any number of numbers in
    # using arbitrary arg
    result = 0
    for num in nums:
        result += num
    return result


def main():
    print("Describe city - use of key arg and default value")
    describe_city("Denver")
    describe_city("Tokyo", "Japan")
    describe_city(country="UK", city="London")
    describe_city("Rome", country="Italy")
    print()
    print("Middle name - use of optional arg")
    print(get_formatted_name(last='Ho', first="Frances"))
    print(get_formatted_name("George", "Yu", middle="Chilun"))
    print()

    # Build person dict - use of dict, zip, opt. arg
    firsts = ['Emily', 'Frances', 'Callum']
    middles = ['Shan-Yi', "", "Robert"]
    lasts = ['Yu', 'Ho', 'Anderson']
    ages = [16, None, 14]
    person_dict = {}
    for first, middle, last, age in zip(firsts, middles, lasts, ages):
        build_person(person_dict, first, last, middle, age)
    print('Build person dict - use of dict, zip, opt. arg')
    print(person_dict)

    # use arbitrary *arg - from module restaurant.py
    # good like toppings or ingredients of recipe
    # or you don't know how many args users will pass in
    # *args will be passed in as tuples (can slice, iterates like list,
    # but is immutable
    r.make_sandwich("Frances", "Chicken", "Tomatoes", "Onions", "Mayo",
                  quantity=2)
    r.make_sandwich("Emily", "BBQ", "Onions", "Mayo")
    r.make_sandwich('George', "Bum Mee", "Hot Peppers")

    # use imported module restaurant (alias r) for functions
    r.make_pizza('Dominic', "pepperoni", 'cheese', 'bacon', size='extra large')
    r.make_drink('Dominic', 'soft drink', size='small')
    r.make_drink('Frances', 'gin and tonic', quantity=2)
    print()

    # using **kwargs - args are passed in key/value pairs in dict
    # we can utilize this to build a dict
    user_profile = build_profile('albert', 'einstein', middle="s",
                                 job='professor', loc='princeton',
                                 age=54)
    print("Albert Einstein profile: \n", user_profile)
    print()
    # using **kwargs - we can use elem in dict to do things
    graph_circle(2, color="blue", thickness=5, fill=True, linestyle="dotted")
    print()

    # using arbitrary arg to pass in any numbers to be summed up
    print(f'sum of integers = {sum_integers(1, 2, 3, 4, 5)}')
    nums_list = [1, 2, 3, 4, 5]
    list2 = [6, 7]
    list3 = [8, 9, 10]
    print("unpacking a list, sum =", sum_integers(*nums_list))
    print("sum of 1-10 =", sum_integers(*nums_list, *list2, *list3))
    print()
    # **kwargs keyword args - passes arbitrary len of vars as dict in
    # key/value pairs


    # ternary operator
    # <expr1> if <cond> else <expr2>
    raining = False
    print("Lets go to the", "beach" if not raining else 'Library')
    raining = True
    print("Lets go to the", "beach" if not raining else 'Library')
    print()

    minor = True
    age = 12 if minor else 18
    print(age)

    # this equals to
    # if a > b:
    #     m = a
    # else:
    #     m = b
    a = 2
    b = 3
    m = a if a > b else b
    print (m)

if __name__ == '__main__':
    main()
