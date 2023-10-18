# Product list and price created under list
product_list = ['TV' , 'Oven' , 'Washer' , 'Microwave' , 'Blender' , 'Stove' , 'Fridge']
price_list = [45 , 40 , 30 , 40 , 20 , 35 , 40]

# Printing the list for user to see and select products
print(product_list)
print(price_list)
my_List = []
plist = []

while True:
        user_input = input('Enter Product name from list or Type exit to quit: ') # Asking user to input product name or type exit to quit

        if user_input.lower() == "exit":
            
            break  # Exit the loop when the user types 'exit'

        try:
            idx = product_list.index(user_input)
            my_List.append(user_input)
            price = price_list[idx]
            print("Your product {} costs {:d}".format(user_input, price))
            plist.append(price) # Adding the user input product price into another list
            a = sum(plist) # Add the amounts of user selected products and place in variable a
            #print(a) # Checking if amounts are appearing correctly 
            #print(plist) # Checking the price in the list
            #print(my_List) # Checking user inputed products appearing correctly in the list
            formatted_output1 = f"${a}" # To display $ sign with the checkout amount
            #print(formatted_output)
            print("Your Checkout Balance is:", formatted_output1) # printing the checkout amount
            if a >= 200: # logic to check the amount of products greater than or equal to $200
                b = a - 50
                #print(b)
                formatted_output2 = f"${b}" # To display $ sign with the final checkout amount after discount
                print("You got $50 discount on your total, Pay: ", formatted_output2) # printing the amount after discount
            else:
                print()
        except ValueError:
            print("Product not in the store")  # If entered something out of the list