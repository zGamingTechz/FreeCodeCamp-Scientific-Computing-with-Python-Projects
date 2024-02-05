def add_expense(expenses, amount, category):
    # Function to add an expense to the list
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    # Function to print all expenses in a formatted way
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    # Function to calculate the total expenses
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    # Function to filter expenses by a specific category
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    # Main program loop
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        # User input for menu choice
        choice = input('Enter your choice: ')

        if choice == '1':
            # Add an expense
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # List all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            # Show total expenses
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            # Filter expenses by category
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            # Exit the program
            print('Exiting the program.')
            break

# Execute the main function
main()
