# Your job is to write a program named ratings.py that:
# Reads the ratings in from the file
# Stores them in a dictionary
# And finally, spits out the ratings in alphabetical order by restaurant

def print_restaurant_ratings(filename):
    """Restaurant rating lister."""

    restaurant_ratings_dict = {}

    # Open the file
    file = open(filename)

    # Iterate over each line
    for line in file:
        line = line.rstrip() # Remove trailing whitespace
        # Assign variables for name and rating
        restaurant_name, rating = line.split(':')[0], line.split(':')[1] 
        restaurant_ratings_dict[restaurant_name] = rating # Add restaurant and rating to dictionary

    # Print each restaurant and its rating in alphabetical order
    for restaurant, rating in sorted(restaurant_ratings_dict.items()):
        print(f'{restaurant} is rated at {rating}.')

print_restaurant_ratings('scores.txt')