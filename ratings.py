# Your job is to write a program named ratings.py that:
# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant
import sys


def read_restaurant_ratings(filename):
    """Take a file and return as a dictionary."""

    restaurant_ratings_dict = {}

    file = open(filename)

    for line in file:
        line = line.rstrip()
        restaurant_name, rating = line.split(':')
        rating = int(rating)
        restaurant_ratings_dict[restaurant_name] = rating
    return restaurant_ratings_dict


def print_restaurant_rating(restaurant_ratings_dict):
    """Takes in dictionary, asks the user how to sort them, and prints the ratings"""

    print('Would you like to view by [R]ating or [N]ame of the restaurant?')
    user_sort_by = input('> ').upper()

    if user_sort_by == 'N':
        for restaurant, rating in sorted(restaurant_ratings_dict.items()):
            print(f'{restaurant} is rated at {rating}.')

    elif user_sort_by == 'R':
        rest_by_ratings_list = sorted(
            restaurant_ratings_dict, key=restaurant_ratings_dict.get, reverse=True)
        for restaurant in rest_by_ratings_list:
            rating = restaurant_ratings_dict[restaurant]
            print(f'{restaurant} is rated at {rating}.')


def get_new_rating():
    """Gets user input for restaurant name, rating and adds it to existing dictionary of ratings"""
    print('Please enter the name of the restaurant you\'d like to review:')
    restaurant_name = input('> ')
    print('Please enter the rating:')
    restaurant_rating = int(input('> '))

    print(f'{restaurant_name} has been added, with a rating of {restaurant_rating}')

    return (restaurant_name, restaurant_rating)


def add_rating(restaurant_ratings_dict, restaurant_name, restaurant_rating):
    """Takes in a dictionary, restaurant, rating and adds the restaurant, rating to the dictionary"""
    restaurant_ratings_dict[restaurant_name] = restaurant_rating


def main(filename):
    print('Welcome to the Restaurant Ratings App')
    restaurant_ratings_dict = read_restaurant_ratings(filename)

    while True:
        print()
        print("""Would you like to 
        [V]iew ratings
        [A]dd a rating
        [Q]uit""")
        user_action = input('> ').upper()
        print()

        if user_action == 'Q':
            break

        elif user_action == 'V':
            print_restaurant_rating(
                restaurant_ratings_dict)

        elif user_action == 'A':
            restaurant_name, restaurant_rating = get_new_rating()
            add_rating(restaurant_ratings_dict,
                       restaurant_name, restaurant_rating)

        else:
            print('Invalid input. Please try again.')


main(sys.argv[1])
