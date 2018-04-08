#Translate text to international morse code as per https://goo.gl/jPGJy6
#and https://morsecode.scphillips.com/morse2.html
#Morse Syntax:
#A dot is represented by .
#A dash is represented by -
#There is no space between parts of the same letter (as the dict shows).
#There is one space between letters and 3 spaces between words.

morse_dict = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
              "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
              "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
              "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
              "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
              "Z": "--..", "1": ".----", "2": "..---", "3": "...--",
              "4": "....-", "5": ".....", "6": "-....", "7": "--...",
              "8": "---..", "9": "----.", "0": "-----", " ": "  ",
              ".": ".-.-.-", ",": "--..--", ":": "---...", "?": "..--..",
              "\"": ".-..-.", "'": ".----.", "-": "-....-", "/": "-..-.",
              "(": "-.--.-", ")": "-.--.-", "@": ".--.-.", "=": "-...-"}

def translate_to_morse():
    """
    Translates text to morse code.
    """
    try:
        translated_morse = ""
        to_translate = input("\nEnter your text here:\n-> ")

        for char in to_translate:
            if char.upper() in morse_dict:
                translated_morse += f"{morse_dict[char.upper()]} "
            else:
                raise ValueError

        return f"\nHere's your morse code:\n{translated_morse}"

    except ValueError:
        print("\nYou've entered a character that is non-alphanumeric or not a punctutation mark. Please try again!")
        return translate_to_morse()

def translate_to_text():
    """
    Translates morse code to text.
    """
    #Inverts the morse_dict dictionary
    text_dict = {}
    for char, morse in morse_dict.items():
        text_dict[morse] = char

    print("\nEnter in your morse code. Please keep the following in mind. There must be a space between every letter and 3 spaces between every word.\n")

    try:
        translated_text = ""
        to_translate = input("Enter your morse code here:\n-> ").split(" ")
        for item in to_translate:
            if item in text_dict:
                translated_text += text_dict[item]
            elif item == "":
                translated_text += " "
            else:
                print(f"\n{item} is not morse code!\n")
                raise ValueError

        #Join and split are used since the 3 spaces in the morse code
        #creates extra spaces in the final string to be output.
        translated_text = " ".join(translated_text.split())
        return f"\nHere's your translation:\n{translated_text}"

    except ValueError:
        print("Please re-enter your morse code! Make sure it's right this time!")
        return translate_to_text()

def use_again():
    """
    Determine if the user wants to use the program again.
    """
    while True:
        try:
            print("\nType [Y] to use the service again or [N] to stop it.")
            answer = input("> ")

            if answer.upper() == "Y":
                return True
            elif answer.upper() == "N":
                return False
            else:
                raise ValueError

        except ValueError:
            print("\nPlease type in either [Y] or [N]. Try again!")
            continue

while True:
    print("Type [T] for Text-to-Morse or [M] for Morse-to-Text.")
    type_of_trans = input("> ")

    if type_of_trans.upper() == "T":
        print(translate_to_morse())
    elif type_of_trans.upper() == "M":
        print(translate_to_text())
    else:
        print("Please restrict your answers to only [T] or [M].\n")
        continue

    if use_again():
        continue
    else:
        break
