import sys
import string


def count_chars(text):
    """
    this function takes a string as a parameter and count the sums of its :
        - characters
        - upper case letters
        - lower case letters
        - punctuation marks
        - spaces
        - digits
    """
    textLength = len(text)
    upperCaseLettersCount = sum(c.isupper() for c in text)
    lowerCaseLettersCount = sum(c.islower() for c in text)
    punctuationCount = sum(c in string.punctuation for c in text)
    spaces = sum(c.isspace() for c in text)
    digits = sum(c.isdigit() for c in text)

    print(f"The text contains {textLength} characters:")
    print(f"{upperCaseLettersCount} upper letters")
    print(f"{lowerCaseLettersCount} lower letters")
    print(f"{punctuationCount} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    This program takes user input or command line argument \
and calls the count_chars function.
    If no argument is provided, it prompts the user to enter a text.
    If more than one argument is provided, it raises an AssertionError.
    """
    args = sys.argv[1:]

    if len(args) > 1:
        raise AssertionError("more than one argument is provided")
    elif len(args) == 0:
        try:
            text = input("What is the text to count?\n")
            text += '\n'
        except EOFError:
            return
    else:
        text = args[0]

    count_chars(text)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError: " + str(e))
