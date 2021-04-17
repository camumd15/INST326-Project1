"""This project will allow you to type in a certain type of food that you want to
eat and it will search through menus to show you what restaurants have that food 
available"""
class Menu:
    """ Initialize the menu of food for each restaurants
    
    Attributes:
    
    dessert (list of dessert): will list dessert options for meals
    food (list of food): will show the option of the entrees that are on the menu
    
    """
    
    # init method for the food and entrees
    def __init__(self, food):
        """ Initialize a new Menu object.

        """
        self.food = food
        self.entrees = set() 

    def restaurantList(self, name):
        """ Prints out a list of restaurants
        
        Args:
            entree (set of entree): a set of new entrees.
            food_list (set of (tuple of str, str)): food and
            corresponding entrees of restaurant.

        Raises:
            ValueError: a restaurant object had an undefined entree attribute.

        Side effects:
            Modifies the value of food_list.

        """
    
    def matchFood(self, vegan, nonvegan):
        """ Take input from the user and read the csv to find what 
            restaurants serve that dish.
        
        Args:
            vegan: a string that return a list of vegan food
            non-vegan: a string that return a list of nonvegan food
        
        Returns:
            return the the type of food if its either vegan or nonvegan
        """

    
    def prices(self, filepath):
        """ The method should read each line from the filepath 
        
        Args:
            filepath = open a file and creates a dictionary list of the file
            self.prices = output the prices of the entree of foods

        Returns:
            returns the tupples in the dictionary if its presents from the list
        """

def main(filename):
    """ It will run the main script of the program 
    
    Args:
        filename (str): A file with other data from the cvs file
        entree (float or int): the prices and type of food from the restaurants
        
    Returns:
        type (float): output different kinds of foods from the list of restaurants 
        
    """

if __name__ == "__main__":  
    main()