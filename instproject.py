"""This project will allow you to type in a certain type of food that you want to
eat and it will search through menus to show you what restaurants have that food 
available"""
class Menu:
    """this class will have the lists of items on the menu to search 
    through when called
    
    Attributes:
    
    Sides (str): will list side options for meals
    Entree (set of food): Will show the option of the entrees that are on the menu
    Dessert (str): Will show a list of the desserts available on the menu
    """
    
    # init method for the food and entrees
    def __init__(self, food):
        """ Initialize a new Menu object. """
        self.food = food
        self.entrees = set() 

    """ this will print out the name of the restaurant that is searched by the user, 
    if the restaurant is on the list it will print the name and if not it will say "Do not have" """
    def restaurantList(self, name):


    """ This will take input from the user and read the csv to find what 
    restaurants serve that dish and return a list of those places.
     """
    def matchFood(self, filename):

        return matches

    """ This will ask the user for a price and if that price is within range of 
    the restaurants, then it will return the names within range """
    def prices(self, filename):
        return inRange

    if __name__ == "__main__":
        args = parse_args(sys.argv[1:]) 