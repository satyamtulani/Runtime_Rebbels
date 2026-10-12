# Shopping Cart Total
# Write a program that calculates the total price of a product based on the product selected and the quantity entered by the user. The program should support the 
# four available products and display the total amount that needs to be paid



# code has a few errors:

# - Product prices are stored as strings, so convert them to integers.
# - `quantity` should be converted to an integer.
# - Each product condition should use its own price.
# - The `else` block should handle invalid product names.
# - Use proper indentation.

### Corrected Python code

# python
# ```

headPhone = 999
smartWatch = 1599
PS5 = 1299
iPad = 599

productName = input("Enter Product Name: ")

quantity = int(input("Enter the Quantity of the Product: "))

if productName == "headPhone":
    totalPrice = headPhone * quantity

elif productName == "smartWatch":
    totalPrice = smartWatch * quantity

elif productName == "PS5":
    totalPrice = PS5 * quantity

elif productName == "iPad":
    totalPrice = iPad * quantity

else:
    print("Invalid Product Name!")
    totalPrice = None

if totalPrice is not None:
    print(f"Total Amount To Be Paid: ₹{totalPrice}")
# ```

### Example output

# text
# ```
# Enter Product Name: PS5
# Enter the Quantity of the Product: 2
# Total Amount To Be Paid: ₹2598
# ```

# Note: Enter the product name exactly as shown in the code, such as `headPhone`, `smartWatch`, `PS5`, or `iPad`.