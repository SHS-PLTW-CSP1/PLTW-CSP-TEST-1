from __future__ import print_function # use Python 3.0 printing

def age_limit_output(age):
    '''Step 6a if-else example'''
    AGE_LIMIT = 13    # convention: use CAPS for constants
    if age < AGE_LIMIT:
      print (age, 'is below the age limit.')
    else:
      print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
    
def report_grade(percent):
    '''Step 6b if-else'''
    mastery = 80
    if percent >= mastery:
        print( 'A grade of ', percent,' indicates mastery.')
        print('Keep up the good work')
    else:
        print ('A grade of ', percent, ' does not indicate mastery.')
        print ('Seek extra practice or help.')

def vowel(letter):
    ''' Step 8 example'''
    vowels = 'aeiouAEIOU'
    if letter in vowels:
      return True
    else:
      return False
# should check len(letter)==1

def letter_in_word(guess,word):
    ''' Step 8 '''
    if guess in word:
        return True
    else:
        return False
        
def hint(color):
    ''' Step 9 '''
    secret = ['red','blue','green','yellow','black','pink']
    if color in secret:
        print('The color ', color, 'IS in the secret sequence of colors.')
    else:
        print('The color ', color,'IS NOT in the secret sequence of colors.')
        
    