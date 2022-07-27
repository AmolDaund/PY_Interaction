
cities_list = ['Mumbai', 'Delhi', 'Bangalore', 'Karnataka', 'Hyderabad']


def decorator(wishOfParameter):
    def inner(parameter):  # Nested Function
        if parameter == 'Soma':
            print('Hi', parameter, 'how are you?')
        else:
            wishOfParameter(parameter)

    return inner


@decorator
def wish(parameter):
    print("Hello", parameter, 'Good morning')


wish("Soma")
wish("Amol")