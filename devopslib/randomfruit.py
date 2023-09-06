from random import choices

def fruit():
    fruits = ['apple','cherry','strawberry']
    return choices(fruits)[0]

def meal(beverage):
    my_fruit = fruit()
    if my_fruit == 'cherry':
        complete_meal = f'Your meal is a {my_fruit} and {beverage}'
        return complete_meal
    alternate_meal = f'Your meal is a {my_fruit} and {beverage}'
    return alternate_meal