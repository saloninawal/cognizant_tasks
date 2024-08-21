import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(message)s')

def log_error(error_message):
    """Log errors with a timestamp."""
    logging.error(error_message)

def process_transaction(transaction_data):
    """Process the transaction data after validation."""
    try:
        # Example: Process transaction
        amount = float(transaction_data['amount'])
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        # Placeholder for transaction processing logic
        print(f"Processed transaction for {transaction_data['customer_name']} of amount {amount}")

    except ValueError as ve:
        log_error(str(ve))
        print(f"Error: {ve}")
    except KeyError as ke:
        log_error(f"Missing data: {ke}")
        print(f"Error: Missing required data {ke}")
    except Exception as e:
        log_error(str(e))
        print(f"An unexpected error occurred: {e}")

def validate_transaction_data(transaction_data):
    """Validate the transaction data before processing."""
    required_fields = ['customer_name', 'amount']

    for field in required_fields:
        if field not in transaction_data or not transaction_data[field]:
            raise KeyError(f"{field} is required and cannot be empty.")

    try:
        amount = float(transaction_data['amount'])
        if amount <= 0:
            raise ValueError("Transaction amount must be a positive number.")
    except ValueError:
        raise ValueError("Invalid amount. Please enter a numeric value.")

def main():
    while True:
        try:
            print("\nTransaction Processing System")
            customer_name = input("Enter customer name: ")
            amount = input("Enter transaction amount: ")

            transaction_data = {
                'customer_name': customer_name,
                'amount': amount
            }

            # Validate transaction data
            validate_transaction_data(transaction_data)

            # Process the transaction
            process_transaction(transaction_data)

        except KeyError as ke:
            log_error(f"Validation error: {ke}")
            print(f"Validation Error: {ke}. Please try again.")
        except ValueError as ve:
            log_error(f"Validation error: {ve}")
            print(f"Validation Error: {ve}. Please try again.")
        except Exception as e:
            log_error(f"Unexpected error: {e}")
            print(f"An unexpected error occurred: {e}")

        # Ask if the user wants to process another transaction
        retry = input("Do you want to process another transaction? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Exiting the system.")
            break

if __name__ == "__main__":
    main()
