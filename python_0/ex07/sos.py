import sys

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}


def encode_to_morse(text):
    """
    Encodes the given text to Morse code.

    Args:
        text (str): The text to be encoded.

    Returns:
        str: The encoded text in Morse code.

    Raises:
        AssertionError: If the text contains characters that are not supported\
            by the Morse code dictionary.
    """
    encoded_text = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            encoded_text += MORSE_CODE_DICT[char] + ' '
        else:
            raise AssertionError("the arguments are bad")
    return encoded_text.strip()


def main():
    args = sys.argv[1:]
    try:
        assert len(args) == 1, "the arguments are bad"
        assert isinstance(args[0], str), "the arguments are bad"
        print(encode_to_morse(args[0]))
    except Exception as e:
        print("AssertionError: " + str(e))


if __name__ == "__main__":
    main()
