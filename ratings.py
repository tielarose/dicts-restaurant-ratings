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


def main(filename):

    restaurant_rating_dict =  read_restaurant_ratings(filename)
    print_restaurant_rating(restaurant_rating_dict)


main(sys.argv[1])
