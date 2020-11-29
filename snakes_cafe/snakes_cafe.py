from textwrap import dedent

food = [
    {"name": "Wings", "count": 0},
    {"name": "Cookies", "count": 0},
    {"name": "Spring Rolls", "count": 0},
    {"name": "Salmon", "count": 0},
    {"name": "Steak", "count": 0},
    {"name": "Meat Tornado", "count": 0},
    {"name": "A Literal Garden", "count": 0},
    {"name": "Ice Cream", "count": 0},
    {"name": "Cake", "count": 0},
    {"name": "Pie", "count": 0},
    {"name": "Coffee", "count": 0},
    {"name": "Tea", "count": 0},
    {"name": "Unicorn Tears", "count": 0}
]

def menu():
    print(
        """
        **************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        ** To quit at any time, type "quit" **
        **************************************

        Appetizers
        ----------
        Wings
        Cookies
        Spring Rolls

        Entrees
        -------
        Salmon
        Steak
        Meat Tornado
        A Literal Garden

        Desserts
        --------
        Ice Cream
        Cake
        Pie

        Drinks
        ------
        Coffee
        Tea
        Unicorn Tears

        ***********************************
        ** What would you like to order? **
        ***********************************
        """
    )

def order():
    item = input("        > ").lower().capitalize()
    for x in food:
        # if item in x.values():
            if (item == x["name"]):
                    x["count"] = x["count"] + 1
                    print("\n        ** %d order of %s have been added to your meal **" % (x["count"] , x["name"]))
                    break
    else:
        print(f"        Sorry! {item.lower()} is not on the menu")
    
def total():
    print("\n        Your order summary: \n")    
    for x in food:
        if (x["count"] > 0):
            print("        Item: %s \t Quantity: %d" % (x["name"] , x["count"]))           
    
    print("\n        Thanks for ordering, enjoy your meal! \n\n")    


if __name__ == "__main__": 
    menu()
    order()
    cont = 'y'
    while cont != 'quit':
        user_input = input("""
        Would you like to order another item?
        Enter any key to continue, or "quit" to exit.
        > """).lower()
        cont = user_input
        if cont == 'quit':
            total()
            break
        cont = ''
        print("        What would you like to add to your order?")
        order()
        
    

        
