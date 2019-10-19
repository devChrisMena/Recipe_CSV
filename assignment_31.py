#Name: Christopher Mena
#Email: christopher.mena66@myhunter.cuny.edu
#Date: October 18, 2019
#Read, modify and display csv user input

#Import libaries 
import pandas as pd

#Take user input
look_recipe = input("Enter recipe name: ")

#Read csv file
recipe = pd.read_csv(look_recipe)
recipe["Amount"] = recipe["Amount"] * 2

#Output

print("Double your recipe is:")
print(recipe)
