# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

user_letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
if user_letter in 'a e i o u':
  print('The letter ', user_letter, 'is a vowel')
else:
  print('The letter ', user_letter, ' is a consonant')

# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = ''
while phrase != 'quit':
  phrase = input('Please enter a word or phrase: ')
  print('What you entered is', len(phrase), ' characters long')

  # exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

human_years = int(input("Input a dog's age in human years: "))
if human_years < 3:
  dog_years = human_years * 10
else:
  dog_years = 20 + (human_years - 2) * 7
print(f"The dog's age in dog years is {dog_years}")


# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

# print('Enter the lengths of three side of a triangle:')
# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

if a == b and b == c:
  print(f'A triangle with sides of {a}, {b} & {c} is an equalateral triangle')
elif a != b and a != c and b != c:
  print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
else:
  print(f'A triangle with sides of {a}, {b} & {c} is an isosceles triangle')

