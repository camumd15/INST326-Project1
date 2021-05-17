from argparse import ArgumentParser
import sys
import pandas as pd
df = pd.read_csv("restaurants.csv")


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
    def __init__(self, name, category, food, gluten, calories, prices):
        """ Initialize a new Menu object.

        """
        self.name = name
        self.category = category
        self.food = food
        self.gluten = gluten
        self.calories = calories
        self.prices = prices 
        
        
            
    def restaurantList(self, restaurant):
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
        if self.name == "Mcdonalds":
            mcdonalds = df["Restaurant"] == "Mcdonalds"
            return mcdonalds
        if self.name == "Hard Times":
            hardTimes = df["Restaurant"] == "Hard Times"
            return hardTimes
        if self.name == "Jersey Mikes":
            jerseyMikes = df["Restaurant"] == "Jersey Mikes"
            return jerseyMikes
        if self.name == "Chipotle":
            chipotle = df["Restaurant"] == "Chipotle"
            return chipotle
        if self.name == "Papa John's":
            papas = df["Restaurant"] == "Papa John's"
            return papas
        if self.name == "Panda Express":
            pandaEx = df["Restaurant"] == "Panda Express"
            return pandaEx

        print(restaurantList())
    
    def matchFood(self, category):
        """ Take input from the user and read the csv to find what 
            restaurants serve that dish."""
        
        """Args:
            vegan: a string that return a list of vegan food
            non-vegan: a string that return a list of nonvegan food
        
        Returns:
            return the the type of food if its either vegan or nonvegan
        """
        if self.category == "Burger":
            burger = df["Restaurant"] == "McDonalds"
            return burger
        if self.category == "Wings":
            wings = df["Restaurant"] == "Hard Times"
            return wings
        if self.category == "Sandwich":
            sandwich = df["Restaurant"] == "Jersey Mikes"
            return sandwich
        if self.category == "Chicken Bowl":
            bowl = df["Restaurant"] == "Chipotle"
            return bowl
        if self.category == "Pizza":
            pizza = df["Restaurant"] == "Papa John's"
            return pizza
        if self.category == "Chinese":
            chinese = df["Restaurant"] == "Panda Express"
            return chinese

        print(matchFood())
    
    def price(self, prices):
        """ The method should read each line from the filepath 
        
        Args:
            cost = shows a file and creates a dictionary list of the file
            self.prices = output the prices of the entree of foods

        Returns:
            returns the tupples in the dictionary if its presents from the list
        """
        
        if self.prices == "Big Mac":
            cost = df["Restaurant"] == 3.99
            return cost
        if self.prices == "Texas Wings":
            cost = df["Restaurant"] == 13.43
            return cost
        if self.prices == "Giant Club Supreme":
            cost = df["Restaurant"] == 15.99
            return cost
        if self.prices == "Chicken Bowl":
            cost = df["Restaurant"] == 6.50
            return cost
        if self.prices == "Pepperoni Pizza":
            cost = df["Restaurant"] == 15.99
            return cost
        if self.prices == "Orange Chicken and Rice":
            cost = df["Restaurant"] == 7.50
            return cost
        
        print(price)
        
    def calories(self, calories):
        """This method will read the column from the csv file and return the
        amount of calories that a specific food has.  
        
        Args:
            amount = shows the column and creates a dictionary of the calories
            self.calories = out the amount of calories for the food item
            
        Returns: 
            returns the amount of calories in the category
        """
        if self.calories == "Burger":
            amount = df["Restaurant"] == 563
            return amount
        if self.calories == "Wings":
            amount = df["Restaurant"] == 954
            return amount
        if self.calories == "Sandwhich":
            amount = df["Restaurant"] == 2140
            return amount
        if self.calories == "Mexican":
            amount = df["Restaurant"] == 390
            return amount
        if self.calories == "Pizza":
            amount = df["Restaurant"] == 2806
            return amount
        if self.calories == "Chinese":
            amount = df["Restaurant"] == 800
            return amount
            
        print(calories)
        
def main(filename):
    """ It will run the main script of the program 
    
    Args:
        filename (str): A file with other data from the cvs file
        entree (float or int): the prices and type of food from the restaurants
        
    Returns:
        type (float): output different kinds of foods from the list of restaurants 
        
    """
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            split = line.split(",")
            if split[0] != "Table 1" and split[0] != "Restaurant ":
                name = split[0]
                category = split[1]
                food = split[2]
                gluten = split[3]
                calories = split[4]
                price = split[5]


    user_input = int(input("If you would like to search for a specific restaurant type 1, If you want to search for a type of food press 2, If you want to search for a specific item from a menu press 3, if you want to see what options are gluten free press 4, if you want to search for foods that are under a certain calorie press 5, and lastly if you want to search for food items under a certain price then press 6."))
    if user_input == 1:
        restaurant_input = input("Which restaurant would you like to choose: Mcdonalds, Hard Times, Jersey Mikes, Chipotle, Papa John's, Panda Express? ")
        return self.restaurantList(restaurant_input)
    elif user_input == 2:       
        type_input = input("What type of food are you looking for: Burger, Wings, Sandwich, Chicken Bowl, Pizza, Chinese? ")
        return self.matchFood(type_input)
    elif user_input == 3:
        item_input = input("What food item are you looking for? ")
        return self.foodtype(item_input)
    elif user_input == 4:
        gluten_input = input("Do you want the food to be gluten free? ")
        return self.gluten(gluten_input)
    elif user_input == 5:
        calories_input = input("What is the maximum number of calories you want to consume? ")
        return self.calories(calories_input)
    elif user_input == 6:
        prices_input = input("What is the maximum you are willing to spend? ")
        return self.prices(prices_input)
    else:
        print("Invalid input")

if __name__ == "__main__":  
    
    main(sys.argv[1])
    