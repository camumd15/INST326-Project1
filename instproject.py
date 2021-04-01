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
    
    def __init__(self, food):
        """ Initialize a new Menu object. """
        self.food = food
        self.entrees = set() 