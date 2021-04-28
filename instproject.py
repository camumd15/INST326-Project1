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
    def __init__(self, restaurant, type, item, gluten, calories, prices):
        """ Initialize a new Menu object.

        """
        self.food = food
        self.entrees = set() 
        user_input = int(input("If you would like to search for a specific restaurant type 1, If you want to search for a type of food press 2, If you want to search for a specific item from a menu press 3, if you want to see what options are gluten free press 4, if you want to search for foods that are under a certain calorie press 5, and lastly if you want to search for food items under a certain price then press 6."))
        if user_input == 1:
            restaurant_input = input("What restaurant are you looking for? ")
            return self.restaurantList(restaurant_input)
        if user_input == 2:
            type_input = input("What type of food are you looking for? ")
            return self.matchFood(type_input)
        if user_input == 3:
            item_input = input("What food item are you looking for? ")
            return self.foodtype(item_input)
        if user_input == 4:
            gluten_input = input("Do you want the food to be gluten free? ")
            return self.gluten(gluten_input)
        if user_input == 5:
            calories_input = input("What is the maximum number of calories you want to consume? ")
            return self.calories(calories_input)
        if user_input == 6:
            prices_input = input("What is the maximum you are willing to spend? ")
            return self.prices(prices_input)
        
        
            
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
            restaurants serve that dish."""
        
        """Args:
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
    def calories(self, filepath):
        """This method will read the column from the csv file and return the
        amount of calories that a specific food has.  
        
        Args:
            filepath = reads the column and creates a dictionary of the calories
            self.calories = out the amount of calories for the food item
            
        Returns: 
            returns the amount of calories in the category"""
    def foodtype(self, filepath):
        "Foodtype"
    def gluten(self, filepath):
        "Whether it is gluten or not"
    
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