def check_if_letter(character):
    """
    Checks if a given character is an alphabet letter.

    Args:
        character (str): The character to check.

    Returns:
        bool: True if the character is a letter, False otherwise.
    """
    if len(character) == 1 and character.isalpha():
        return True
    else:
        return False

# Get input from the user
user_input = input("Enter a character: ")

# Check if the input is a letter and print the result
if check_if_letter(user_input):
    print(f"'{user_input}' is a letter.")
else:
    print(f"'{user_input}' is not a letter.")