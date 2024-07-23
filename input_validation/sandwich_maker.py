import pyinputplus as pyip

print("""
    Let's make sandwich! Please, select availible options: 
""")

bread = pyip.inputMenu(['wheat', 'white', 'sourdough', ], numbered=True)
protein = pyip.inputMenu(['chicken', 'ham', 'turkey', 'tofu'], numbered=True)
cheese_option = pyip.inputYesNo("Would you like to add cheese?")
if cheese_option:
    cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozarella', ], numbered=True)
else:
    cheese = "out cheese"

souce_option = pyip.inputYesNo("Would you like to add souce?")
if souce_option: 
    souce = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'], numbered=True)
else:
    souce = "out souce"
number_of_sandwiches = pyip.inputInt("How many sandwiches you want?")
print(f"""Thank you for order! You've ordered: {number_of_sandwiches} 
{bread} sandwich with {protein} with 
{cheese} and with {souce} souce""")

