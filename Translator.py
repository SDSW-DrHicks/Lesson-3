# ----------------------------------------------------------
# Construct a Translator
# ----------------------------------------------------------

# This exercise is meant to challenge you to use functions
# and nested loops and if statements to create an app which could
# exchange the vowels of a phrase to another character.

# --------------------------------------
# Key
# --------------------------------------

def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEUIOaeiou":
            translation = translation + "x"
        else:
            translation = translation + letter
    return translation

print(translate(input("Ender a phrase: ")))