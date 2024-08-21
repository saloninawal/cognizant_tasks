# text_processing_tool.py

def count_words(text):
    """Counts the number of words in the given text."""
    words = text.split()
    return len(words)

def find_unique_words(text):
    """Finds unique words in the given text."""
    words = text.split()
    unique_words = set(words)
    return unique_words

def convert_to_uppercase(text):
    """Converts the given text to uppercase."""
    return text.upper()

def main():
    """Main function to interact with the user and process text."""
    text = input("Enter a text string: ")

    print("\nChoose a text processing option:")
    print("1. Count Words")
    print("2. Find Unique Words")
    print("3. Convert to Uppercase")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        word_count = count_words(text)
        print(f"Word Count: {word_count}")
    elif choice == "2":
        unique_words = find_unique_words(text)
        print(f"Unique Words: {unique_words}")
    elif choice == "3":
        uppercase_text = convert_to_uppercase(text)
        print(f"Uppercase Text: {uppercase_text}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
