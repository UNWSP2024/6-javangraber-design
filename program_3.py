# Programmer: Javan Graber
# Date: 2/25/2026
# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

# Create a function that calculates the total county sales tax
def calculate_county_tax(monthly_sales):
    # Calculate the total county sales using the formula
    total_county_sales_tax = monthly_sales * .025
    # Return the total county sales tax
    return total_county_sales_tax

# Create a function that calculates the total state sales tax
def calculate_state_tax(monthly_sales):
    total_state_sales_tax = monthly_sales * .05
    return total_state_sales_tax

# Create the main function that asks for the sales, displays the previous taxes, and
# calculates the total tax
def main():
    # Ask for the monthly sales
    monthly_sales = float(input('Enter the monthly sales: '))

    # Call for the county tax function and display the total county sales tax
    total_county_sales_tax = calculate_county_tax(monthly_sales)
    print(f'The total county sales tax is ${total_county_sales_tax:.2f}')

    # Call for the state tax function and display the total state sales tax
    total_state_sales_tax = calculate_state_tax(monthly_sales)
    print(f'The total state sales tax is ${total_state_sales_tax:.2f}')

    # Calculate the total tax by adding the state and county sales tax
    total_tax = total_county_sales_tax + total_state_sales_tax
    print(f'The total sales tax is ${total_tax:.2f}')

# Call for the main function
main()
