"""This project will allow you to type in a certain type of food that you want to
eat and it will search through menus to show you what restaurants have that food 
available"""
class Menu:
    """ Initialize the menu of food for each restaurants
    
    Attributes:
    
    sides (lis of sides): will list side options for meals
    entree (list of food): Will show the option of the entrees that are on the menu
    dessert (list of dessert): Will show a list of the desserts available on the menu
    
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
            name (set of name): a set of new students.
            food_list (set of (tuple of str, str)): food and
            corresponding name addresses of restaurant.

        Raises:
            ValueError: a restaurant object had an undefined name attribute.

        Side effects:
            Modifies the value of food_list.

        """
    
    def matchFood(self, flavor):
        """ Take input from the user and read the csv to find what 
            restaurants serve that dish.
        
        Args:
        
        Returns:
        
        """

    
    def prices(self, filename):
        """ Ask the user for a price input and if that price is within range of 
            the restaurants
        
        Args:
        
        Returns:
        
        """
        

def main():
    """ Run the program
    
    Args:
    
    Side Effects:
    
    """

if __name__ == "__main__":  
    main()