from argparse import ArgumentParser
import sys
import pandas as pd
df = pd.read_csv("restaurants.csv")


"""This project will allow the user to search through various restaurants
using different categories of search. The menu will then be returned of the restaurants that 
meet the specifications"""
class Menu:
    """ Initialize the menu of food for each restaurants
    
    Attributes:
    
    name: name of the restaurant
    category: type of food served
    food: menu item served
    gluten: if the item is gluten free
    calories: number of calories in the item
    prices: how much the item costs
    
    """
    
    # init method for the food and entrees
    def __init__(self, name, category, food, gluten, calories, prices):
        """ Initialize a new Menu object.

        """
        self.name = name
        self.category = category
        self.food = food
        self.gluten = gluten
        self.calories = calories
        self.prices = prices 
        
        
            
def restaurantList(menus, restaurant):
    """ returns the restaurant chosen by the user
        
    Args:
        name: the name of the restaurant chosen

    Raises:
        ValueError: a restaurant object had an undefined entree attribute.

    Side effects:
        Modifies the value finalmenu.

    """
    finalmenu = []
    for menu in menus:
        if menu.name == restaurant:
            finalmenu.append(menu)
    return finalmenu
    
def matchFood(menus, category):
    """ Take input from the user and read the csv to find what 
        restaurants serve that type of food."""
        
    """Args:
        category: the type of food that is served
        
    Returns:
        return the restaurants that serve that type of food
    """
    finalmenu = []
    for menu in menus:
        if menu.category == category:
            finalmenu.append(menu)
    return finalmenu

    
def gluten_method(menus, gluten):
    finalmenu = []
    for menu in menus:
        if menu.gluten == gluten:
            finalmenu.append(menu)
    return finalmenu

def foodtype(menus, item):
    finalmenu = []
    for menu in menus:
        if menu.food == item:
            finalmenu.append(menu)
    return finalmenu

def price_method(menus, price):
    """ The method should read each line from the filepath 
        
    Args:
        cost = shows a file and creates a dictionary list of the file
        menu.prices = output the prices of the entree of foods

    Returns:
        returns the menus of restaurants that serve food for under the user specified amount
    """
    finalmenu = []
    for menu in menus:
        if menu.prices <= price:
            finalmenu.append(menu)
    return finalmenu    
   
        
        
def calories_method(menus, calorie):
    """This method will read the column from the csv file and return the
    amount of calories that a specific food has.  
        
    Args:
        amount = shows the column and creates a dictionary of the calories
        self.calories = out the amount of calories for the food item
            
    Returns: 
        returns the amount of calories in the category
    """
    
            
    finalmenu = []
    for menu in menus:
        if menu.prices <= calorie:
            finalmenu.append(menu)
    return finalmenu
        
def main(filename):
    """ It will run the main script of the program 
    
    Args:
        filename (str): A file with other data from the cvs file
        entree (float or int): the prices and type of food from the restaurants
        
    Returns:
        type (float): output different kinds of foods from the list of restaurants 
        
    """
    menus = []
   
    with open(filename, 'r', encoding = 'utf-8') as f:
        lines = f.readlines()[2:]
        f.close()
        for line in lines:
            split = line.split(",")
            if split is not None and split[0] != "Table 1" and split[0] != "Restaurant ":
                name = split[0]
                category = split[1]
                food = split[2]
                gluten = split[3]
                calories = int(split[4])
                price = float(split[5])
                menu = Menu(name, category, food, gluten, calories, price)
                menus.append(menu)
                


    user_input = int(input("If you would like to search for a specific restaurant type 1, \n If you want to search for a type of food press 2, \n If you want to search for a specific item from a menu press 3, \n if you want to see what options are gluten free press 4, \n if you want to search for foods that are under a certain calorie press 5, \n and lastly if you want to search for food items under a certain price then press 6."))
    if user_input == 1:
        restaurant_input = input("Which restaurant would you like to choose: Mcdonalds, Hard Times, Jersey Mikes, Chipotle, Papa John's, Panda Express? ")
        menu = restaurantList(menus, restaurant_input)
    elif user_input == 2:       
        type_input = input("What type of food are you looking for: Burger, Wings, Sandwich, Mexican, Pizza, Chinese? ")
        menu = matchFood(menus, type_input)
    elif user_input == 3:
        item_input = input("What food item are you looking for? This will show the menu with that food item. The options are Big Mac, 12 Texas Wings, Giant Club Supreme, Chicken Bowl, Pepperoni Pizza, Orange Chicken and Rice. ")
        menu = foodtype(menus, item_input)
    elif user_input == 4:
        gluten_input = input("Do you want the food to be gluten free? This will show menus with your specified gluten request")
        menu = gluten_method(menus, gluten_input)
    elif user_input == 5:
        calories_input = int(input("What is the maximum number of calories you want to consume? This will show menus with items under this calorie count. "))
        menu = calories_method(menus, calories_input)
    elif user_input == 6:
        prices_input = float(input("What is the maximum you are willing to spend? This will show menus with items under this price. "))
        menu = price_method(menus, prices_input)
    else:
        print("Invalid input")
    printmethod(menu)    
        
        

def printmethod(menus):
    for menu in menus:
        print(f"This is the menu for {menu.name}, the food is {menu.food}, is the item Gluten Free? {menu.gluten} the item has {menu.calories} calories, and the item costs {menu.prices}")
        

if __name__ == "__main__":  
    
    main(sys.argv[1])
    