# Your job is to write a program named ratings.py that:
# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant
import sys

def read_restaurant_ratings(filename):
    """Take a file and return as a dic."""

    restaurant_ratings_dict = {}

    # Open the file
    file = open(filename)

    # Iterate over each line
    for line in file:
        line = line.rstrip() # Remove trailing whitespace
        # Assign variables for name and rating
        restaurant_name, rating = line.split(':')[0], line.split(':')[1] 
        restaurant_ratings_dict[restaurant_name] = rating # Add restaurant and rating to dictionary
    
    return restaurant_ratings_dict


def print_restaurant_rating(restaurant_ratings_dict):
    """takes in dic and printing the rating in alphabetical order"""

    # Print each restaurant and its rating in alphabetical order

    for restaurant, rating in sorted(restaurant_ratings_dict.items()):
        print(f'{restaurant} is rated at {rating}.')

def get_new_rating():
    print('Welcome! Please enter the name of the restaurant you\'d like to review:')
    restaurant_name = input('> ')
    print('Please enter the rating:')
    restaurant_rating = float(input('> '))

    return (restaurant_name, restaurant_rating)

def add_rating(restaurant_ratings_dict, restaurant_name, restaurant_rating):
    """Takes in a dictionary, restaurant, rating and adds the restaurant, rating to the dictionary"""
    restaurant_ratings_dict[restaurant_name] = restaurant_rating



def main(filename):
    # Create a dictionary of ratings from the file
    restaurant_ratings_dict =  read_restaurant_ratings(filename)

    # Print the ratings alphabetically by restaurant
    print_restaurant_rating(restaurant_ratings_dict)

    # As the user for a restaurant name and rating
    restaurant_name, restaurant_rating = get_new_rating()

    # Add user input to existing dictionary of ratings
    add_rating(restaurant_ratings_dict, restaurant_name, restaurant_rating)

    # Reprint the ratings alphabetically by restaurant
    print_restaurant_rating(restaurant_ratings_dict)



main(sys.argv[1])
