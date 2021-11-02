#Create an array 'Days'
Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Firday', 'Saturday', 'Sunday']
print(Days[4:7])
 
#Create an array 'Vowels'
Vowels = ['a', 'e', 'i', 'o', 'u']
 
user_vowel = str(input("Please insert a vowel: "))
if len(user_vowel) > 1:
    print("Please only enter one character")
else: 
    if user_vowel == 'a' or user_vowel == 'e' or user_vowel == 'i' or user_vowel == 'o' or user_vowel == 'u':
        print("That is a vowel!")
    else:
        print("Sorry, that is not a vowel.")
        if user_vowel.isalpha():
            print("That is a consonant, not a vowel.")
        elif user_vowel.isdigit():
